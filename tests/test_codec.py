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
            print(i, j)

            xrow, yrow, xcol, ycol = search_seqs(s)
            print(xrow, yrow, xcol, ycol)
            assert yrow >= 0 and xcol >= 0

            s = helpers.rot90_cw(s)
            xrow, yrow, xcol, ycol = search_seqs(s)
            print(xrow, yrow, xcol, ycol)
            assert yrow == -1 and xcol >= 0

            s = helpers.rot90_cw(s)
            xrow, yrow, xcol, ycol = search_seqs(s)
            print(xrow, yrow, xcol, ycol)
            assert yrow == -1 and xcol == -1

            print("-----")
            s = helpers.rot90_cw(s)
            xrow, yrow, xcol, ycol = search_seqs(s)
            print(xrow, yrow, xcol, ycol)
            xrow, yrow, xcol, ycol = search_seqs(s, 1)
            print(xrow, yrow, xcol, ycol)
            xrow, yrow, xcol, ycol = search_seqs(s, 2)
            print(xrow, yrow, xcol, ycol)
            xrow, yrow, xcol, ycol = search_seqs(s, 3)
            print(xrow, yrow, xcol, ycol)
            assert yrow >= 0 and xcol == -1

    # mat = helpers.rot90_cw(s)
    # t = mat[:8, :8]
    # print_search(t, 90)

    # mr = helpers.rot90_cw(mr)
    # t = mr[:8, :8]
    # print_search(t, 180)

    # mr = helpers.rot90_cw(mr)
    # t = mr[:8, :8]
    # print_search(t, 270)

    # print(s[:, 0, 0], t[:, 0, 0])
    # print(s[:, 0, 1], t[:, 0, 1])
    # print(s[0, :, 0], t[0, :, 0])
    # print(s[0, :, 1], t[0, :, 1])

    # for y in range(256 - 8):
    #     for x in range(256 - 8):
    #         s = m[y : y + 8, x : x + 8]
    #         for k in range(4):
    #             r = np.rot90(s, k=k, axes=(0, 1))
    #             kfix = anoto.decode_rotation(r)
    #             if k != ((4 - kfix) % 4):
    #                 print(y, x, k)
    #             assert k == ((4 - kfix) % 4)

    # s = m[34 : 34 + 8, 79 : 79 + 8]
    # r = np.rot90(s, k=1, axes=(0, 1))
    # kfix = anoto.decode_rotation(r)
    # print(kfix)
    # assert k == ((4 - kfix) % 4)
