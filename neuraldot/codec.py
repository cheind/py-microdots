import numpy as np

from . import integer


def _make_cyclic(seq: np.ndarray, order: int) -> np.ndarray:
    """Appends the first order-1 characters to make cyclic positions locatable."""
    return np.concatenate((seq, seq[: order - 1]))


class AnotoEncoder:
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
        self.mns_order = mns_order
        self.sns_order = mns_order - 1  # number of delta
        self.sns = [np.asarray(s, dtype=np.int8) for s in sns]
        self.sns_lengths = [len(s) for s in self.sns]
        self.sns_cyclic = [_make_cyclic(s, self.sns_order) for s in self.sns]
        self.num_basis = integer.NumberBasis(pfactors)
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
            roll = self._compute_mns_roll(x, roll)
            s = np.roll(self.mns, -roll)
            m[:, x, 0] = np.tile(s, ytiles)

        # y-direction
        roll = section[1] % self.mns_length
        xtiles = mshape[1] // self.mns_length
        for y in range(mshape[0]):
            roll = self._compute_mns_roll(y, roll)
            s = np.roll(self.mns, -roll)
            m[y, :, 1] = np.tile(s, xtiles)

        return m[: shape[0], : shape[1]]

    def _compute_mns_roll(self, pos: int, prev_roll: int) -> int:
        if pos == 0:
            return prev_roll

        # To find the roll of MNS for pos, we need to determine
        # the delta corresponding to [pos-1,pos]
        delta = self._compute_deltae(pos - 1)[0]
        return (prev_roll + delta.item()) % self.mns_length

    def _compute_deltae(self, pos: int) -> np.ndarray:
        """Computes 5 delta values between [pos,pos+5]."""

        # Compute the remainders for each of the secondary number
        # sequences. Each remainder is the position in the
        # corresponding secondary sequence.
        rs = np.remainder(pos, self.sns_lengths)

        # Extract the coefficients
        coeffs = np.array(
            [s[r : r + self.sns_order] for s, r in zip(self.sns_cyclic, rs)],
            dtype=np.int32,
        )  # (num_sns, num_coeff)
        deltae = self.num_basis.reconstruct(coeffs.T) + self.delta_range[0]
        return deltae


class AnotoDecoder:
    def __init__(
        self,
        mns: list[int],
        mns_order: int,
        sns: list[list[int]],
        pfactors: list[int],
        delta_range: tuple[int, int],
    ) -> None:
        self.mns = np.asarray(mns, dtype=np.int8)
        self.mns_cyclic = _make_cyclic(mns, order=mns_order).tobytes()
        self.mns_length = len(self.mns)
        self.mns_order = mns_order
        self.sns_order = mns_order - 1  # number of delta
        self.sns = [np.asarray(s, dtype=np.int8) for s in sns]
        self.sns_lengths = [len(s) for s in self.sns]
        self.sns_cyclic = [_make_cyclic(s, self.sns_order).tobytes() for s in self.sns]
        self.num_basis = integer.NumberBasis(pfactors)
        self.crt = integer.CRT(self.sns_lengths)
        self.delta_range = delta_range

    def decode_bitmatrix(self, bits: np.ndarray) -> tuple[int, int]:
        """Decodes the (N,M,2) bitmatrix into a unique xy location corresponding
        to the upper-left element."""
        assert bits.shape[0] >= self.mns_order and bits.shape[1] >= self.mns_order
        bits = bits[
            : self.mns_order, : self.mns_order
        ]  # in case a bigger matrix is given
        bits = bits.astype(np.int8)
        xy = (
            self._decode_bitmatrix_direction(bits[..., 0].T),
            self._decode_bitmatrix_direction(bits[..., 1]),
        )

        # TODO: compute section values.

        return xy

    def _decode_bitmatrix_direction(self, bits: np.ndarray) -> int:
        """Decodes the position along a single direction.

        It is assumed that the MNS is along rows. So, if you decode the x-direction
        make sure to transpose the bitmatrix before passing to this method.
        """

        # Compute the 6 locations in the MNS via byte matching
        locs = np.array(
            [self.mns_cyclic.find(s.tobytes()) for s in bits], dtype=np.int32
        )

        if (locs < 0).any():
            raise ValueError("Decoding error")

        # Compute the 5 differences modulo the length of MNS
        deltae = np.remainder(locs[1:] - locs[:-1], self.mns_length)
        if not np.logical_and(
            deltae >= self.delta_range[0], deltae <= self.delta_range[1]
        ).all():
            raise ValueError("Decoding error")

        # Find 5 a1...a4 coefficients by integer division
        deltae -= self.delta_range[0]
        coeffs = self.num_basis.project(deltae).astype(
            np.int8
        )  # (mns_order,num_sns) array

        # Find the locations of substring coefficients.
        ps = [s.find(a.tobytes()) for s, a in zip(self.sns_cyclic, coeffs.T)]

        # find smallest positive p such that the congruences
        # p1 = p mod 236
        # p2 = p mod 233
        # p3 = p mod 31
        # p4 = p mod 241
        # According to the chinese remainder theorem there
        # p will be unique for p < L.
        # TODO explain how the system of equations is solved.

        p = self.crt.solve(ps)
        return p
