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

References:
Anoto AB  "Method and device for decoding a position-coding pattern"
https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf

Aboufadel, Edward, Timothy Armstrong, and Elizabeth Smietana.
"Position coding." arXiv preprint arXiv:0706.0869 (2007).
"""
A4 = np.array(
    [
        0,0,0,0,0,1,0,2,0,0,0,0,2,0,0,2,0,1,0,
        0,0,1,1,2,0,0,0,1,2,0,0,2,1,0,0,0,2,1,
        1,2,0,1,0,1,0,0,1,2,1,0,0,1,0,0,2,2,0,
        0,0,2,2,1,0,2,0,1,1,0,0,1,1,1,0,1,0,1,
        1,0,1,2,0,1,1,1,1,0,0,2,0,2,0,1,2,0,2,
        2,0,1,0,2,1,0,1,2,1,1,0,1,1,1,2,2,0,0,
        1,0,1,2,2,2,0,0,2,2,2,0,1,2,1,2,0,2,0,
        0,1,2,2,0,1,1,2,1,0,2,1,1,0,2,0,2,1,2,
        0,0,1,1,0,2,1,2,1,0,1,0,2,2,0,2,1,0,2,
        2,1,1,1,2,0,2,1,1,1,0,2,2,2,2,0,2,0,2,
        2,1,2,1,1,1,1,2,1,2,1,2,2,2,1,0,0,2,1,
        2,2,1,0,1,1,2,2,1,1,2,1,2,2,2,2,1,2,0,
        1,2,2,1,2,2,0,2,2,2,1,1,1
    ]
)

# fmt: on
