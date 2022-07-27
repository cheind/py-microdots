import numpy as np
import pytest

from neuraldot import defaults


def test_bitmatrix_encode_different_sections():
    enc = defaults.anoto_encoder_6x6_a4_fixed

    m = enc.encode_bitmatrix((60, 60), section=(0, 0))
    assert m.shape == (60, 60, 2)
    assert np.all(m[:8, 0, 0] == (0, 0, 0, 0, 0, 0, 1, 0))
    assert np.all(m[0, :8, 1] == (0, 0, 0, 0, 0, 0, 1, 0))

    m = enc.encode_bitmatrix((60, 60), section=(1, 1))
    assert m.shape == (60, 60, 2)
    assert np.all(m[:8, 0, 0] == (0, 0, 0, 0, 0, 1, 0, 0))
    assert np.all(m[0, :8, 1] == (0, 0, 0, 0, 0, 1, 0, 0))


@pytest.mark.parametrize(
    "size,section",
    [
        (256, (0, 0)),
        (256, (10, 10)),
    ],
)
def test_bitmatrix_decode(size, section):
    enc = defaults.anoto_encoder_6x6_a4_fixed
    dec = defaults.anoto_decoder_6x6_a4_fixed

    m = enc.encode_bitmatrix((size, size), section=section)
    assert m.shape == (size, size, 2)

    for y in range(size - 6):
        for x in range(size - 6):
            xy = dec.decode_bitmatrix(m[y : y + 6, x : x + 6])
            assert xy == (x, y)


def test_bitmatrix_decode_fail_origa4():
    enc = defaults.anoto_encoder_6x6
    dec = defaults.anoto_decoder_6x6

    # works
    m = enc.encode_bitmatrix((256, 256), section=(0, 0))
    xy = dec.decode_bitmatrix(m[0:, 216:])
    assert xy == (216, 0)

    # first error, because A4 is not debruijn.
    # issue is that coefficients position search in A4
    # gives wrong location because of duplicate substrings
    # (see substring 1 1 2 1 2 at index 195 and 217)
    xy = dec.decode_bitmatrix(m[0:, 217:])
    assert xy != (217, 0)
    assert xy == (139779713, 0)
