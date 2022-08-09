import numpy as np
import pytest

from neuraldot import codec, mini_sequences


@pytest.mark.parametrize(
    "size,section",
    [
        (256, (0, 0)),
        (256, (10, 10)),
    ],
)
def test_bitmatrix_decode_mini(size, section):
    anoto = codec.AnotoCodec(
        mini_sequences.MNS,
        4,
        [mini_sequences.A1, mini_sequences.A2],
        [3, 5],
        (0, 15),
    )

    m = anoto.encode_bitmatrix((size, size), section=section)
    assert m.shape == (size, size, 2)

    for y in range(size - 6):
        for x in range(size - 6):
            xy = anoto.decode_bitmatrix(m[y : y + 6, x : x + 6])
            assert xy == (x, y)
