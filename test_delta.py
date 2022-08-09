import numpy as np
import pytest

from neuraldot import defaults


def test_bitmatrix_decode():
    codec = defaults.anoto_6x6_a4_fixed

    m = codec.encode_bitmatrix((6, 20), section=(0, 0))


test_bitmatrix_decode()
