"""Original and modified Anoto sequences.

This module contains (cut-down, quasi) De Bruijn sequences used
in Anoto products according to Anoto patents. These sequences
can be used together with the encoder/decoder class to recreate
Anoto patterns.

In total there are 5 different sequences required
    - The Main Number Sequence (NMS)
    - Four secondary number sequences A1,...,A4

Each sequence is a cut-down or quasi De Bruijn sequence meaning
that each substring appears _at most_ once.

## A4 sequence issues
The A4 sequence is supposed to be a quasi De Bruijn sequence. However,
the sequence given in one of the patents has an incorrect length. Some
authors have appended a missing 1 coefficient to fix that. However, my
tests reveal that the sequence isn't De Bruijn to begin with. Multiple
substrings of length 5 appear twice (see tests for details). This leads
to possible decoding errors as early as position 217.

Therefore, this module contains an additional sequence (A4_alt) that
I've created which has the De Bruijn property intact. However, since it
is quasi De Bruijn, some of the substrings of order 5 are missing and
I do not have the tools to check wether the missing substrings might
actually appear in a coded pattern.

Using A4_alt will also break compatibility to existing Anoto tech.

## References
Anoto AB  "Method and device for decoding a position-coding pattern"
https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf

Özgür, Ayberk. Cellulo: Tangible haptic swarm robots for learning.
Diss. Ecole Polytechnique Fédérale de Lausanne, 2018.

Aboufadel, Edward, Timothy Armstrong, and Elizabeth Smietana.
"Position coding." arXiv preprint arXiv:0706.0869 (2007).
"""

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

# Original A4 that is not De Bruijn.
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
    ],
    dtype=np.int8
)

# Alternative A4 added by myself which is De Bruijn of correct length,
# but might miss needed substrings of length 5 that actually appear 
# in a decoding.
A4_alt = np.array([0, 0, 0, 0, 2, 2, 2, 2, 0, 2, 2, 2, 1, 0, 2, 2, 2, 0, 0, 2, 2, 1,
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

# fmt: on
