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


def test_rot90_cw():
    bits = np.random.randint(0, 2, size=(12, 12, 2))
    b = bits
    for i in range(4):
        b = helpers.rot90_cw(b)
    assert np.allclose(bits, b)


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
