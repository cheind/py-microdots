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

# fmt: on
