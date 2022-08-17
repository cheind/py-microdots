import numpy as np

from microdots import helpers

from . import integer
from .exceptions import DecodingError


def _make_cyclic(seq: np.ndarray, order: int) -> np.ndarray:
    """Appends the first order-1 characters to make cyclic positions
    locatable."""
    return np.concatenate((seq, seq[: order - 1]))


class AnotoCodec:
    """A generalized implementation of the Anoto coding.

    An instance of this class supports encoding and decoding
    of Anoto patterns. In particular, given a bit-matrix of
    shape (M,M,2) the provided methods decode a) the position
    coordindate (x,y), b) the section coordindates (u,v) and
    the pattern orientation as explained in [1]. When encoding,
    the class generates a bit-matrix (H,W,2) for a specific
    section.

    References:
        [1] Christoph Heindl, 'py-microdots and the Anoto Codec',
        2022
    """

    def __init__(
        self,
        mns: list[int],
        mns_order: int,
        sns: list[list[int]],
        pfactors: list[int],
        delta_range: tuple[int, int],
    ) -> None:
        """Initialize the Anoto codec.

        Params
            mns: a binary quasi de Bruijn sequence QB(2,n,m) of order n and
                length m that acts as the main number sequence (MNS).
            mns_order: the order or the MNS.
            sns: a list of secondary number sequences which are also
                quasi de Bruijn sequences or order n-1. The lengths
                of these sequences should be relatively prime.
            delta_range: a range possible difference values.
            pfactors: the sequence of prime factors to decompose
                difference values into.
        """
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
        """Generates a (H,W,2) bitmatrix given section coordindates (u,v).

        Params:
            shape: (H,W) pattern shape
            section: section coordinates to use

        Returns
            bits: (H,W,2) matrix of encoded position coordinates.
        """
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
        """Computes and returns the MNS offset for the next postion
        given the previous offset."""
        if pos == 0:
            return prev_roll

        # To find the roll of MNS for pos, we need to determine
        # the delta corresponding to [pos-1,pos]
        return (prev_roll + self._delta(pos - 1)) % self.mns_length

    def _integrate_roll(self, pos: int, first_roll: int) -> int:
        """Computes the MNS offset for the given position
        from offsets for zero position.

        This method is of complexity O(pos) due to required
        integration of all previous positions.
        """
        r = 0
        for i in range(0, pos):
            r += self._delta(i)
        return (first_roll + r) % self.mns_length

    def _delta(self, pos: int):
        """Computes the difference value between pos and pos+1."""

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

    def decode_rotation(self, bits: np.ndarray) -> int:
        """Determines the rotation of pattern in 90° steps (ccw).

        This method helps to determine the rotation of the pattern
        in 90° steps. A value of 0 indicates that the pattern orientation
        is canonical. A value of 1 means that the pattern is rotated by
        90° in ccw orientation and a helpers.rot90(bits, k=-1) can bring
        it into canonical orientation.

        For this to work, usually larger bitmatrices than for decoding
        the location are required. For the default Anoto 6x6 pattern,
        8x8 matrices have to be used.
        """

        # Make matrix square
        M = min(bits.shape[0], bits.shape[1])
        bits = bits[:M, :M].astype(np.int8)

        # Test each of the four possible ccw rotations by attempting
        # to locate partial sequences in the MNS
        def check_rot(rotbits):
            M = rotbits.shape[0]
            xcol_correct = 0
            yrow_correct = 0

            for i in range(M):
                xcol = self.mns_cyclic_bytes.find(rotbits[:, i, 0].tobytes())
                yrow = self.mns_cyclic_bytes.find(rotbits[i, :, 1].tobytes())
                xcol_correct += 1 if xcol >= 0 else 0
                yrow_correct += 1 if yrow >= 0 else 0

            return xcol_correct >= M // 2 and yrow_correct >= M // 2

        for k in range(4):
            rotbits = helpers.rot90(bits, k=k)
            if check_rot(rotbits):
                return (4 - k) % 4

        raise DecodingError("Failed to determine pattern orientation.")

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

    def _assert_bitmatrix_shape(self, bits: np.ndarray, min_size: int = None):
        if bits.ndim != 3:
            raise DecodingError(f"Excepted a (M,N,2) matrix, but got {bits.shape}")
        N, M, C = bits.shape
        if min_size is None:
            min_size = self.mns_order
        if N < min_size or M < min_size or C != 2:
            raise DecodingError(
                f"Excepted at least a matrix of size ({min_size},{min_size},2) matrix,"
                f" but got {bits.shape}"
            )

    def decode_section(self, bits: np.ndarray, pos: tuple[int, int]) -> tuple[int, int]:
        """Computes the section coordinates from an observed bits matrix.

        Params:
            bits: (M,M,2) matrix of observed bits
            pos: position coordinates (x,y)

        Returns:
            coords: section coordinates (u,v)
        """
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
        sx = self._integrate_roll(pos[0], first_roll=0)
        sy = self._integrate_roll(pos[1], first_roll=0)

        return (
            (px_mns - pos[1] - sx) % self.mns_length,
            (py_mns - pos[0] - sy) % self.mns_length,
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
