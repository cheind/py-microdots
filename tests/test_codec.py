import numpy as np
import pytest

from neuraldot import defaults, codec, helpers


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
            xy = anoto.decode_location(m[y : y + 6, x : x + 6])
            assert xy == (x, y)
            if step % 10 == 0:  # less impact on test performance
                sec = anoto.decode_section(m[y : y + 6, x : x + 6], xy)
                assert sec == section
            step += 1


def test_bitmatrix_decode_fail_origa4():
    anoto = defaults.anoto_6x6

    # works
    m = anoto.encode_bitmatrix((256, 256), section=(0, 0))
    xy = anoto.decode_location(m[0:, 216:])
    assert xy == (216, 0)

    # first error, because A4 is not debruijn.
    # issue is that coefficients position search in A4
    # gives wrong location because of duplicate substrings
    # (see substring 1 1 2 1 2 at index 195 and 217)
    xy = anoto.decode_location(m[0:, 217:])
    assert xy != (217, 0)
    assert xy == (139779713, 0)


def test_bit_packing():

    nums = np.arange(4).astype(np.uint8)
    bits = codec.num_to_bits(nums)
    assert np.allclose(bits, [[0, 0], [1, 0], [0, 1], [1, 1]])

    bits = np.random.randint(0, 2, size=(10, 10, 2))
    nums = codec.bits_to_num(bits)
    rbits = codec.num_to_bits(nums)
    assert np.allclose(bits, rbits)


def vote_axes(anoto, mat):
    xcol_correct = 0
    yrow_correct = 0

    for i in range(8):
        xcol = anoto.mns_cyclic_bytes.find(mat[:, i, 0].tobytes())
        yrow = anoto.mns_cyclic_bytes.find(mat[i, :, 1].tobytes())
        xcol_correct += 1 if xcol >= 0 else 0
        yrow_correct += 1 if yrow >= 0 else 0

    return xcol_correct >= 4 and yrow_correct >= 4


def test_bitmatrix_decode_orientation():
    anoto = defaults.anoto_6x6_a4_fixed
    m = anoto.encode_bitmatrix((256, 256), section=(5, 10))

    def search_seqs(mat, idx=0):
        mat = mat.astype(np.int8)
        xcol = anoto.mns_cyclic_bytes.find(mat[:, idx, 0].tobytes())
        ycol = anoto.mns_cyclic_bytes.find(mat[:, idx, 1].tobytes())
        xrow = anoto.mns_cyclic_bytes.find(mat[idx, :, 0].tobytes())
        yrow = anoto.mns_cyclic_bytes.find(mat[idx, :, 1].tobytes())
        return xrow, yrow, xcol, ycol

    for i in range(256 - 8):
        for j in range(256 - 8):
            s = m[i : i + 8, j : j + 8].copy()
            # print(i, j)
            assert vote_axes(anoto, s)

            s = helpers.rot90_cw(s)
            assert not vote_axes(anoto, s)

            s = helpers.rot90_cw(s)
            assert not vote_axes(anoto, s)

            s = helpers.rot90_cw(s)
            assert not vote_axes(anoto, s)
