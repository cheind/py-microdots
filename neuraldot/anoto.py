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
    ]
)

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
    ]
)
CA1 = np.concatenate((A1, A1[:4]))

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
    ]
)
CA2 = np.concatenate((A2, A2[:4]))

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
    ]
)
CA3 = np.concatenate((A3, A3[:4]))

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

References:
Anoto AB  "Method and device for decoding a position-coding pattern"
https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf

Aboufadel, Edward, Timothy Armstrong, and Elizabeth Smietana.
"Position coding." arXiv preprint arXiv:0706.0869 (2007).
"""
A4 = np.array(
    [
        0,0,0,0,0,1,0,2,0,0,0,0,2,0,0,2,0,1,0,0,0,1,1,2,0,0,0,
        1,2,0,0,2,1,0,0,0,2,1,1,2,0,1,0,1,0,0,1,2,1,0,0,1,0,0,2,2,0,0,
        0,2,2,1,0,2,0,1,1,0,0,1,1,1,0,1,0,1,1,0,1,2,0,1,1,1,1,0,0,2,0,
        2,0,1,2,0,2,2,0,1,0,2,1,0,1,2,1,1,0,1,1,1,2,2,0,0,1,0,1,2,2,2,
        0,0,2,2,2,0,1,2,1,2,0,2,0,0,1,2,2,0,1,1,2,1,0,2,1,1,0,2,0,2,1,
        2,0,0,1,1,0,2,1,2,1,0,1,0,2,2,0,2,1,0,2,2,1,1,1,2,0,2,1,1,1,0,
        2,2,2,2,0,2,0,2,2,1,2,1,1,1,1,2,1,2,1,2,2,2,1,0,0,2,1,2,2,1,0,
        1,1,2,2,1,1,2,1,2,2,2,2,1,2,0,1,2,2,1,2,2,0,2,2,2,1,1,1
    ]
)
CA4 = np.concatenate((A4, A4[:4]))

MNS_LENGTH = len(MNS) # 63
SECONDARY_SEQUENCE_LENGTHS = (len(A1), len(A2), len(A3), len(A4))
A_BASES = np.array([1, 3, 3 * 3, 2 * 3 * 3]).reshape(1, 4)

# fmt: on


def compute_mns_roll(pos: int, prev_roll: int):
    if pos == 0:
        return prev_roll
    rs = np.remainder(pos - 1, SECONDARY_SEQUENCE_LENGTHS)
    abits = np.array(
        [seq[r : r + 5] for seq, r in zip((CA1, CA2, CA3, CA4), rs)]
    )  # (4,5)
    delta = A_BASES @ abits[:, 0:1] + 5  # [5,58]
    return (prev_roll + delta.item()) % MNS_LENGTH


def generate_bitmatrix(shape: tuple[int, int], section=(0, 0)):
    # find multiples of 63 for ease of generation
    mshape = (
        int(63 * np.ceil(shape[0] / 63)),
        int(63 * np.ceil(shape[1] / 63)),
    )
    m = np.empty(mshape + (2,))
    # x-direction
    roll = section[0]
    ytiles = mshape[0] // 63
    for x in range(mshape[1]):
        roll = compute_mns_roll(x, roll)
        s = np.roll(MNS, -roll)
        m[:, x, 0] = np.tile(s, ytiles)

    # y-direction
    roll = section[1]
    xtiles = mshape[1] // 63
    for y in range(mshape[0]):
        roll = compute_mns_roll(x, roll)
        s = np.roll(MNS, -roll)
        m[y, :, 1] = np.tile(s, xtiles)

    return m[: shape[0], : shape[1]]


# def encode(x: int, section_start: int = 0):

#     rs = [x % length for length in SECONDARY_LENGTHS]
#     ds = np.array([seq[r : r + 5] for seq, r in zip((CA1, CA2, CA3, CA4), rs)])
#     deltae = A_BASES @ ds + 5  # [5,58]
#     #integrate to positions
#     mns_pos = x-section_start


#     # print(deltae)
#     return deltae


if __name__ == "__main__":

    np.set_printoptions(threshold=np.inf)
    m = generate_bitmatrix((32, 16))
    print(repr(m[..., 0]))
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
