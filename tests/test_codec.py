import numpy as np
import pytest

from microdots import defaults, codec, helpers


def test_bitmatrix_encode_different_sections():
    anoto = defaults.anoto_6x6_a4_fixed

    m = anoto.encode_bitmatrix((60, 60), section=(0, 0))
    assert m.shape == (60, 60, 2)
    assert np.all(m[:8, 0, 0] == (0, 0, 0, 0, 0, 0, 1, 0))
    assert np.all(m[0, :8, 1] == (0, 0, 0, 0, 0, 0, 1, 0))

    m = anoto.encode_bitmatrix((60, 60), section=(1, 1))
    assert m.shape == (60, 60, 2)
    assert np.all(m[:8, 0, 0] == (0, 0, 0, 0, 0, 1, 0, 0))
    assert np.all(m[0, :8, 1] == (0, 0, 0, 0, 0, 1, 0, 0))


@pytest.mark.parametrize(
    "size,section",
    [
        (256, (0, 0)),
        (256, (10, 5)),
        (256, (5, 10)),
    ],
)
def test_bitmatrix_decode(size, section):
    anoto = defaults.anoto_6x6_a4_fixed

    m = anoto.encode_bitmatrix((size, size), section=section)
    assert m.shape == (size, size, 2)

    step = 0
    for y in range(size - 6):
        for x in range(size - 6):
            xy = anoto.decode_position(m[y : y + 6, x : x + 6])
            assert xy == (x, y)
            if step % 10 == 0:  # less impact on test performance
                sec = anoto.decode_section(m[y : y + 6, x : x + 6], xy)
                assert sec == section
            step += 1


def test_bitmatrix_decode_fail_origa4():
    anoto = defaults.anoto_6x6

    # works
    m = anoto.encode_bitmatrix((256, 256), section=(0, 0))
    xy = anoto.decode_position(m[0:, 216:])
    assert xy == (216, 0)

    # first error, because A4 is not debruijn.
    # issue is that coefficients position search in A4
    # gives wrong location because of duplicate substrings
    # (see substring 1 1 2 1 2 at index 195 and 217)
    xy = anoto.decode_position(m[0:, 217:])
    assert xy != (217, 0)
    assert xy == (139779713, 0)


def test_bitmatrix_decode_rotation():
    anoto = defaults.anoto_6x6_a4_fixed
    m = anoto.encode_bitmatrix((256, 256), section=(5, 10))

    for i in range(128 - 8):
        for j in range(128 - 8):
            s = m[i : i + 8, j : j + 8].copy()

            assert anoto.decode_rotation(s) == 0

            r = helpers.rot90(s, k=1)
            assert anoto.decode_rotation(r) == 1

            r = helpers.rot90(s, k=2)
            assert anoto.decode_rotation(r) == 2

            r = helpers.rot90(s, k=3)
            assert anoto.decode_rotation(r) == 3
