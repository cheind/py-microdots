import numpy as np
import pytest

from neuraldot import helpers


def test_bit_packing():

    nums = np.arange(4).astype(np.uint8)
    bits = helpers.num_to_bits(nums)
    assert np.allclose(bits, [[0, 0], [1, 0], [0, 1], [1, 1]])

    bits = np.random.randint(0, 2, size=(10, 10, 2))
    nums = helpers.bits_to_num(bits)
    rbits = helpers.num_to_bits(nums)
    assert np.allclose(bits, rbits)


def test_rot90_identity():

    bits = np.random.randint(0, 2, size=(12, 12, 2))
    rbits = helpers.rot90(bits, k=4)
    assert np.allclose(bits, rbits)

    rbits = helpers.rot90(bits, k=-4)
    assert np.allclose(bits, rbits)

    rbits = helpers.rot90(bits, k=0)
    assert np.allclose(bits, rbits)


def test_rot90():
    # NW
    # ES
    nums = np.array([[0, 1], [2, 3]], dtype=np.uint8)
    bits = helpers.num_to_bits(nums)

    # 90° ccw
    # array becomes
    # WS
    # NE
    # bits become
    # SE
    # WN
    r = helpers.rot90(bits, k=1)
    assert np.allclose(helpers.bits_to_num(r), [[3, 2], [1, 0]])

    # 90° cw
    # array becomes
    # EN
    # SW
    # bits become
    # SE
    # WN
    r = helpers.rot90(bits, k=-1)
    assert np.allclose(helpers.bits_to_num(r), [[3, 2], [1, 0]])

    # 180° ccw/cw
    # array becomes
    # SE
    # WN
    # bits become
    # NW
    # ES
    r = helpers.rot90(bits, k=2)
    assert np.allclose(helpers.bits_to_num(r), [[0, 1], [2, 3]])
    r = helpers.rot90(bits, k=-2)
    assert np.allclose(helpers.bits_to_num(r), [[0, 1], [2, 3]])

    # 270° ccw/cw
    r = helpers.rot90(bits, k=3)
    ri = helpers.rot90(bits, k=-1)
    assert np.allclose(r, ri)
    r = helpers.rot90(bits, k=-1)
    ri = helpers.rot90(bits, k=3)
    assert np.allclose(r, ri)


# def test_bitmatrix_decode_orientation():
#     anoto = defaults.anoto_6x6_a4_fixed

#     m = anoto.encode_bitmatrix((256, 256), section=(5, 10))

#     # for y in range(256 - 8):
#     #     for x in range(256 - 8):
#     #         s = m[y : y + 8, x : x + 8]
#     #         for k in range(4):
#     #             r = np.rot90(s, k=k, axes=(0, 1))
#     #             kfix = anoto.decode_rotation(r)
#     #             if k != ((4 - kfix) % 4):
#     #                 print(y, x, k)
#     #             assert k == ((4 - kfix) % 4)

#     s = m[34 : 34 + 8, 79 : 79 + 8]
#     r = np.rot90(s, k=1, axes=(0, 1))
#     kfix = anoto.decode_rotation(r)
#     print(kfix)
#     # assert k == ((4 - kfix) % 4)
