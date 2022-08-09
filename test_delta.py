import numpy as np
import pytest

from neuraldot import defaults


def test_bitmatrix_decode():
    codec = defaults.anoto_6x6_a4_fixed

    m = codec.encode_bitmatrix((6, 63), section=(1, 2))

    for x in range(63 - 5):
        print("x", x, codec.decode_section(m[:, x : x + 7], (x, 0)))


test_bitmatrix_decode()
