import numpy as np

from . import integer
from .exceptions import DecodingError


def _make_cyclic(seq: np.ndarray, order: int) -> np.ndarray:
    """Appends the first order-1 characters to make cyclic positions
    locatable."""
    return np.concatenate((seq, seq[: order - 1]))


class AnotoCodec:
    def __init__(
        self,
        mns: list[int],
        mns_order: int,
        sns: list[list[int]],
        pfactors: list[int],
        delta_range: tuple[int, int],
    ) -> None:
        self.mns = np.asarray(mns, dtype=np.int8)
        self.mns_length = len(self.mns)
        self.mns_cyclic = _make_cyclic(mns, order=mns_order)
        self.mns_cyclic_bytes = self.mns_cyclic.tobytes()
        self.mns_order = mns_order
        self.sns_order = mns_order - 1  # number of delta
        self.sns = [np.asarray(s, dtype=np.int8) for s in sns]
        self.sns_lengths = [len(s) for s in self.sns]
        self.sns_cyclic = [_make_cyclic(s, self.sns_order) for s in self.sns]
        self.sns_cyclic_bytes = [seq.tobytes() for seq in self.sns_cyclic]
        self.num_basis = integer.NumberBasis(pfactors)
        self.crt = integer.CRT(self.sns_lengths)
        self.delta_range = delta_range

    def encode_bitmatrix(
        self, shape: tuple[int, int], section: tuple[int, int] = (0, 0)
    ) -> np.ndarray:
        """Generates a NxMx2 bitmatrix encoding x,y positions."""
        # Find nearest multiples of MNS length for ease of generation
        mshape = (
            int(self.mns_length * np.ceil(shape[0] / self.mns_length)),
            int(self.mns_length * np.ceil(shape[1] / self.mns_length)),
        )
        m = np.empty(mshape + (2,), dtype=np.int8)
        # x-direction
        roll = section[0] % self.mns_length
        ytiles = mshape[0] // self.mns_length
        for x in range(mshape[1]):
            roll = self._next_roll(x, roll)
            s = np.roll(self.mns, -roll)
            m[:, x, 0] = np.tile(s, ytiles)

        # y-direction
        roll = section[1] % self.mns_length
        xtiles = mshape[1] // self.mns_length
        for y in range(mshape[0]):
            roll = self._next_roll(y, roll)
            s = np.roll(self.mns, -roll)
            m[y, :, 1] = np.tile(s, xtiles)

        return m[: shape[0], : shape[1]]

    def _next_roll(self, pos: int, prev_roll: int) -> int:
        if pos == 0:
            return prev_roll

        # To find the roll of MNS for pos, we need to determine
        # the delta corresponding to [pos-1,pos]
        return (prev_roll + self._delta(pos - 1)) % self.mns_length

    def _integrate_roll(self, pos: int, first_roll: int) -> int:
        r = 0
        for i in range(0, pos):
            r += self._delta(i)
        return (first_roll + r) % self.mns_length

    def _delta(self, pos: int):
        # Compute the remainders for each of the secondary number
        # sequences. Each remainder is the position in the
        # corresponding secondary sequence.
        rs = np.remainder(pos, self.sns_lengths)

        # Extract the coefficients
        coeffs = np.array(
            [s[r] for s, r in zip(self.sns_cyclic, rs)],
            dtype=np.int8,
        )
        delta = self.num_basis.reconstruct(coeffs[None, :])[0] + self.delta_range[0]
        return delta

    def decode_location(self, bits: np.ndarray) -> tuple[int, int]:
        """Decodes the (N,M,2) bitmatrix into a 2D location.

        The location is with respect to the section tile. The section tiling info
        can be computed afterwards using decode_section.

        Params:
            bits: (N,M,2) matrix of bits. N,M need to be greater than or
                equal to order of MNS.

        Returns:
            loc: 2D (x,y) location wrt to section coordinate system
        """
        bits = np.asarray(bits)
        self._assert_bitmatrix_shape(bits)
        # in case a bigger matrix is given
        bits = bits[: self.mns_order, : self.mns_order].astype(np.int8)

        x = self._decode_location_along_direction(bits[..., 0].T)
        y = self._decode_location_along_direction(bits[..., 1])

        return (x, y)

    def _assert_bitmatrix_shape(self, bits: np.ndarray):
        if bits.ndim != 3:
            raise DecodingError(f"Excepted a (M,N,2) matrix, but got {bits.shape}")
        N, M, C = bits.shape
        if N < self.mns_order or M < self.mns_order or C != 2:
            raise DecodingError(f"Excepted a (M,N,2) matrix, but got {bits.shape}")

    def decode_section(self, bits: np.ndarray, loc: tuple[int, int]) -> tuple[int, int]:
        bits = np.asarray(bits)
        self._assert_bitmatrix_shape(bits)
        px_mns = self.mns_cyclic_bytes.find(
            bits[: self.mns_order, 0, 0].astype(np.int8).tobytes()
        )
        py_mns = self.mns_cyclic_bytes.find(
            bits[0, : self.mns_order, 1].astype(np.int8).tobytes()
        )

        if (px_mns < 0) or (py_mns < 0):
            raise DecodingError("Failed to find partial sequence in MNS.")

        # As _integrate_roll is expensive, decode_section should be called rarely.
        sx = self._integrate_roll(loc[0], first_roll=0)
        sy = self._integrate_roll(loc[1], first_roll=0)

        return (
            (px_mns - loc[1] - sx) % self.mns_length,
            (py_mns - loc[0] - sy) % self.mns_length,
        )

    def _decode_location_along_direction(self, bits: np.ndarray) -> int:
        """Decodes the position along a single direction.

        It is assumed that the MNS is along rows. So, if you decode the x-direction
        make sure to transpose the bitmatrix before passing to this method.

        Params:
            bits: (M,M) matrix where M equals the order of the MNS sequence. It is
                assumed that the MNS is repeated along rows of the given matrix. That
                is, for decoding the x-direction one should transpose the bitmatrix
                before passing it to this method.

        Returns:
            pos: position along the direction up to an unknown section tile.
        """

        # Compute the mns_order locations in the MNS via byte matching
        locs = np.array(
            [self.mns_cyclic_bytes.find(s.tobytes()) for s in bits], dtype=np.int32
        )

        if (locs < 0).any():
            raise DecodingError("Failed to find at least one partial sequence in MNS")

        # Compute the 5 differences modulo the length of MNS
        deltae = np.remainder(locs[1:] - locs[:-1], self.mns_length)
        if not np.logical_and(
            deltae >= self.delta_range[0], deltae <= self.delta_range[1]
        ).all():
            raise DecodingError("At least one delta value is not within required range")

        # Find 5 a1...a4 coefficients by integer division
        deltae -= self.delta_range[0]
        coeffs = self.num_basis.project(deltae).astype(
            np.int8
        )  # (mns_order-1,num_sns) array

        # Find the locations of unique sns_order substring coefficients, these
        # are the remainders to the unknown location.
        ps = [s.find(a.tobytes()) for s, a in zip(self.sns_cyclic_bytes, coeffs.T)]

        p = self.crt.solve(ps)
        return p
