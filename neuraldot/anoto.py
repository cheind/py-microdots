from email.mime import base
import numpy as np


# fmt: off
"""Main number sequence.

A quasi De Bruijn sequence of order 6 and length 63. In a quasi De Bruijn
sequence of order n, each possible substring of length n appears _at most_
once.

References:
Anoto AB  "Method and device for decoding a position-coding pattern"
https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf

Aboufadel, Edward, Timothy Armstrong, and Elizabeth Smietana.
"Position coding." arXiv preprint arXiv:0706.0869 (2007).
"""
MNS = np.array(
    [
        0,0,0,0,0,0,1,0,0,1,1,1,1,1,0,1,0,0,
        1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,
        1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,
        1,1,1,1,0,0,0,1,1
    ],
    dtype=np.int8
)

"""Cyclic version of MNS sequence."""
CMNS = np.concatenate((MNS, MNS[:5]))

"""Converted to bytes for fast index lookup of sub-arrays."""
CMNS_bytes = CMNS.tobytes()

"""
Secondary number sequence for the a1 coefficient.

A quasi De Bruijn sequence of order 5 and length 236. In a quasi De Bruijn
sequence of order n, each possible substring of length n appears _at most_
once.

References:
Anoto AB  "Method and device for decoding a position-coding pattern"
https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf

Aboufadel, Edward, Timothy Armstrong, and Elizabeth Smietana.
"Position coding." arXiv preprint arXiv:0706.0869 (2007).
"""
A1 = np.array(
    [
        0,0,0,0,0,1,0,0,0,0,2,0,1,0,0,1,0,1,0,
        0,2,0,0,0,1,1,0,0,0,1,2,0,0,1,0,2,0,0,
        2,0,2,0,1,1,0,1,0,1,1,0,2,0,1,2,0,1,0,
        1,2,0,2,1,0,0,1,1,1,0,1,1,1,1,0,2,1,0,
        1,0,2,1,1,0,0,1,2,1,0,1,1,2,0,0,0,2,1,
        0,2,0,2,1,1,1,0,0,2,1,2,0,1,1,1,2,0,2,
        0,0,1,1,2,1,0,0,0,2,2,0,1,0,2,2,0,0,1,
        2,2,0,2,0,2,2,1,0,1,2,1,2,1,0,2,1,2,1,
        1,0,2,2,1,2,1,2,0,2,2,0,2,2,2,0,1,1,2,
        2,1,1,0,1,2,2,2,2,1,2,0,0,2,2,1,1,2,1,
        2,2,1,0,2,2,2,2,2,0,2,1,2,2,2,1,1,1,2,
        1,1,2,0,1,2,2,1,2,2,0,1,2,1,1,1,1,2,2,
        2,0,0,2,1,1,2,2
    ],
    dtype=np.int8
)

"""Cylcic version of A1."""
CA1 = np.concatenate((A1, A1[:4]))
"""Sequence as bytes for fast index lookup of sub-arrays."""
CA1_bytes = CA1.tobytes()

"""
Secondary number sequence for the a2 coefficient.

A quasi De Bruijn sequence of order 5 and length 233. In a quasi De Bruijn
sequence of order n, each possible substring of length n appears _at most_
once.

References:
Anoto AB  "Method and device for decoding a position-coding pattern"
https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf

Aboufadel, Edward, Timothy Armstrong, and Elizabeth Smietana.
"Position coding." arXiv preprint arXiv:0706.0869 (2007).
"""
A2 = np.array(
    [
        0,0,0,0,0,1,0,0,0,0,2,0,1,0,0,1,0,1,0,
        1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,2,0,
        0,0,1,2,0,1,0,1,2,1,0,0,0,2,1,1,1,0,1,
        1,1,0,2,1,0,0,1,2,1,2,1,0,1,0,2,0,1,1,
        0,2,0,0,1,0,2,1,2,0,0,0,2,2,0,0,1,1,2,
        0,2,0,0,2,0,2,0,1,2,0,0,2,2,1,1,0,0,2,
        1,0,1,1,2,1,0,2,0,2,2,1,0,0,2,2,2,1,0,
        1,2,2,0,0,2,1,2,2,1,1,1,1,1,2,0,0,1,2,
        2,1,2,0,1,1,1,2,1,1,2,0,1,2,1,1,1,2,2,
        0,2,2,0,1,1,2,2,2,2,1,2,1,2,2,0,1,2,2,
        2,0,2,0,2,1,1,2,2,1,0,2,2,0,2,1,0,2,1,
        1,0,2,2,2,2,0,1,0,2,2,1,2,2,2,1,1,2,1,
        2,0,2,2,2
    ],
    dtype=np.int8
)

"""Cyclic version of A1 sequence."""
CA2 = np.concatenate((A2, A2[:4]))

"""Cyclic A2 as converted to bytes for fast lookup of sub-arrays."""
CA2_bytes = CA2.tobytes()

"""
Secondary number sequence for the a3 coefficient.

A quasi De Bruijn sequence of order 5 and length 31. In a quasi De Bruijn
sequence of order n, each possible substring of length n appears _at most_
once.

References:
Anoto AB  "Method and device for decoding a position-coding pattern"
https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf

Aboufadel, Edward, Timothy Armstrong, and Elizabeth Smietana.
"Position coding." arXiv preprint arXiv:0706.0869 (2007).
"""
A3 = np.array(
    [
        0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,0,0,
        1,0,1,0,1,1,0,1,1,1,0,1
    ],
    dtype=np.int8
)
"""Cyclic version of A3 sequence."""
CA3 = np.concatenate((A3, A3[:4]))

"""Cyclic A3 as converted to bytes for fast lookup of sub-arrays."""
CA3_bytes = CA3.tobytes()

"""
Secondary number sequence for the a4 coefficient.

A quasi De Bruijn sequence of order 5 and length 241. In a quasi De Bruijn
sequence of order n, each possible substring of length n appears _at most_
once.

TODO: This sequence is strange. According to the patent it has only 240 digits and
not 241. However 241 are required for math.lcm(236,233,31,241) to be 410815348. In
some codes (libdots) it seems like a 1 is appended to make it 241. However, that 
breaks the quasi De Bruijn property and multiple 5 long sequences reappear (e.g
[1 1 1 0 0] appears at pos 82 and 238 (cylcic) for more see the test). Best choice 
would be to append a 0, which would give 237 unique substrings instead of 241. For 
now I leave the 1 appended, since this is what most codes do.

Currently we use a custom 241 length cut-down de Bruijn sequence generated by 
http://debruijnsequence.org/db/cutdown. While tests are ok, I wonder if the sequence
might have dropped some sequences of length 5 that appear in decoding?

References:
Anoto AB  "Method and device for decoding a position-coding pattern"
https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf

Aboufadel, Edward, Timothy Armstrong, and Elizabeth Smietana.
"Position coding." arXiv preprint arXiv:0706.0869 (2007).
"""
# A4 = np.array(
#     [
#         0,0,0,0,0,1,0,2,0,0,0,0,2,0,0,2,0,1,0,0,0,1,1,2,0,0,0,
#         1,2,0,0,2,1,0,0,0,2,1,1,2,0,1,0,1,0,0,1,2,1,0,0,1,0,0,2,2,0,0,
#         0,2,2,1,0,2,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,2,0,1,1,1,1,0,0,2,0,
#         2,0,1,2,0,2,2,0,1,0,2,1,0,1,2,1,1,0,1,1,1,2,2,0,0,1,0,1,2,2,2,
#         0,0,2,2,2,0,1,2,1,2,0,2,0,0,1,2,2,0,1,1,2,1,0,2,1,1,0,2,0,2,1,
#         2,0,0,1,1,0,2,1,2,1,0,1,0,2,2,0,2,1,0,2,2,1,1,1,2,0,2,1,1,1,0,
#         2,2,2,2,0,2,0,2,2,1,2,1,1,1,1,2,1,2,1,2,2,2,1,0,0,2,1,2,2,1,0,
#         1,1,2,2,1,1,2,1,2,2,2,2,1,2,0,1,2,2,1,2,2,0,2,2,2,1,1,1
#     ],
#     dtype=np.int8
# )
A4 = np.array([0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 1, 0, 2, 2, 2, 0, 0, 2, 2, 1,
       2, 0, 2, 2, 1, 1, 0, 2, 2, 1, 0, 0, 2, 2, 0, 0, 0, 2, 1, 2, 2, 0,
       2, 1, 2, 1, 0, 2, 1, 2, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 1, 0, 2, 1,
       1, 0, 0, 2, 1, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 2, 1, 0, 2, 0, 2, 0,
       0, 2, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 2, 2, 2, 0, 1, 2, 2, 1, 0, 1,
       2, 2, 0, 0, 1, 2, 1, 2, 0, 1, 2, 1, 1, 0, 1, 2, 1, 0, 0, 1, 2, 0,
       0, 0, 1, 1, 2, 2, 0, 1, 1, 2, 1, 0, 1, 1, 2, 0, 0, 1, 1, 1, 2, 0,
       1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 2, 1, 2,
       2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0,
       0, 0, 1, 0, 2, 2, 0, 1, 0, 2, 1, 0, 1, 0, 2, 0, 0, 1, 0, 1, 2, 0,
       2, 0, 1, 2, 0, 1, 0, 1, 1, 0, 2, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1], dtype=np.int8)

"""Cyclic version of A4 sequence."""
CA4 = np.concatenate((A4, A4[:4]))

"""Cyclic A4 as converted to bytes for fast lookup of sub-arrays."""
CA4_bytes = CA4.tobytes()

MNS_LENGTH = len(MNS) # 63
SECONDARY_SEQUENCE_LENGTHS = (len(A1), len(A2), len(A3), len(A4))
L = np.prod(SECONDARY_SEQUENCE_LENGTHS)
A_BASES = np.array([1, 3, 3 * 3, 2 * 3 * 3])

# fmt: on


class Anoto:
    def __init__(self) -> None:
        self.sns_lengths = (len(A1), len(A2), len(A3), len(A4))
        self.a_bases = np.array([1, 3, 3 * 3, 2 * 3 * 3])
        self.qs = np.array([135, 145, 17, 62])
        self.L = np.prod(self.sns_lengths)

    def encode_bitmatrix(self, shape: tuple[int, int], section=(0, 0)) -> np.ndarray:
        """Generates a NxMx2 bitmatrix encoding x,y positions."""
        # find multiples of 63 for ease of generation
        mshape = (
            int(63 * np.ceil(shape[0] / 63)),
            int(63 * np.ceil(shape[1] / 63)),
        )
        m = np.empty(mshape + (2,), dtype=np.int8)
        # x-direction
        roll = section[0] % 63
        ytiles = mshape[0] // 63
        for x in range(mshape[1]):
            roll = self._compute_mns_roll(x, roll)
            s = np.roll(MNS, -roll)
            m[:, x, 0] = np.tile(s, ytiles)

        # y-direction
        roll = section[1] % 63
        xtiles = mshape[1] // 63
        for y in range(mshape[0]):
            roll = self._compute_mns_roll(y, roll)
            s = np.roll(MNS, -roll)
            m[y, :, 1] = np.tile(s, xtiles)

        return m[: shape[0], : shape[1]]

    def _compute_mns_roll(self, pos: int, prev_roll: int) -> int:
        if pos == 0:
            return prev_roll

        # To find the roll of MNS for pos, we need to determine
        # the delta corresponding to [pos-1,pos]
        delta = self._compute_deltae(pos - 1)[0]
        return (prev_roll + delta.item()) % MNS_LENGTH

    def _compute_deltae(self, pos: int) -> np.ndarray:
        """Computes 5 delta values between [pos,pos+5]."""
        rs = np.remainder(pos, self.sns_lengths)

        abits = np.array(
            [seq[r : r + 5] for seq, r in zip((CA1, CA2, CA3, CA4), rs)], dtype=np.int32
        )  # (4,5)
        delta = self.a_bases.reshape(1, 4) @ abits + 5  # [5,58]
        return delta.reshape(-1)  # (5,)

    def decode_bitmatrix(self, bits: np.ndarray) -> tuple[int, int]:
        """Decodes the (N,M,2) bitmatrix into a unique xy location corresponding to the upper-left element."""
        assert bits.shape[0] >= 6 and bits.shape[1] >= 6
        bits = bits[:6, :6]  # in case a bigger matrix is given
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
        loc_MNS = np.array([CMNS_bytes.find(s.tobytes()) for s in bits], dtype=np.int32)
        # Compute the 5 differences modulo the length of MNS
        deltae = np.remainder(loc_MNS[1:] - loc_MNS[:-1], len(MNS))
        if not np.logical_and(deltae >= 5, deltae <= 58).all():
            raise ValueError("Decoding error")

        # Find 5 a1...a4 coefficients by integer division
        deltae -= 5
        a4 = deltae // self.a_bases[3]
        deltae = np.remainder(deltae, self.a_bases[3])
        a3 = deltae // self.a_bases[2]
        deltae = np.remainder(deltae, self.a_bases[2])
        a2 = deltae // self.a_bases[1]
        deltae = np.remainder(deltae, self.a_bases[1])
        a1 = deltae // self.a_bases[0]

        # Find the 4 locations of substrings of length 5
        p1 = CA1_bytes.find(a1.astype(np.int8).tobytes())
        p2 = CA2_bytes.find(a2.astype(np.int8).tobytes())
        p3 = CA3_bytes.find(a3.astype(np.int8).tobytes())
        p4 = CA4_bytes.find(a4.astype(np.int8).tobytes())
        # print(p1, p2, p3, p4)

        # find smallest positive p such that the congruences
        # p1 = p mod 236
        # p2 = p mod 233
        # p3 = p mod 31
        # p4 = p mod 241
        # According to the chinese remainder theorem there
        # p will be unique for p < L.
        # TODO explain how the system of equations is solved.

        p = 0
        p += self.L // self.sns_lengths[0] * p1 * self.qs[0]
        p += self.L // self.sns_lengths[1] * p2 * self.qs[1]
        p += self.L // self.sns_lengths[2] * p3 * self.qs[2]
        p += self.L // self.sns_lengths[3] * p4 * self.qs[3]
        return p % self.L


if __name__ == "__main__":

    anoto = Anoto()
    m = anoto.encode_bitmatrix(shape=(32, 32), section=(0, 0))

    # np.set_printoptions(threshold=np.inf)
    # m = generate_bitmatrix((32, 16), section=(10, 10))

    print(anoto.decode_bitmatrix(m[0:, 0:]))

    # r = 0
    # for i in range(10):
    #     r = compute_mns_roll(i, r)
    #     print(i, r)

    # maxd = 0
    # mind = 1000
    # for i in range(0, 1000):
    #     d = encode(i)
    #     maxd = max(maxd, d.max())
    #     mind = min(mind, d.min())

    # print(mind, maxd)
