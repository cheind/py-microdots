from typing import Literal
import numpy as np


def bits_to_num(bitmatrix: np.ndarray) -> np.ndarray:
    # Little order: x is lowest bit, y is highes bit => 10 = 2 means x=0,y=1
    # x,y,num, dir,
    # 0,0, 0, north
    # 1,0, 1, west
    # 0,1, 2, east
    # 1,1, 3, south
    return np.packbits(bitmatrix, axis=-1, bitorder="little").squeeze(-1)


def num_to_bits(num_matrix: np.ndarray) -> np.ndarray:
    return np.unpackbits(
        np.expand_dims(num_matrix, -1), axis=-1, count=2, bitorder="little"
    )


"""Maps from displacement direction d to canonical direction c.
For example index d=1 ('west') -> c=3."""
NUM2DIR = [0, 3, 1, 2]

"""Reverse of NUM2DIR."""
DIR2NUM = [0, 2, 3, 1]


def rot90(
    bitmatrix: np.ndarray,
    k: int = 1,
) -> np.ndarray:
    """Simulates 90° rotation of the bitmatrix applied k-times.

    When k is positive applies a counterclockwise rotation,
    else clockwise.
    """
    m = bits_to_num(bitmatrix)
    # 1. Rotate array
    m = np.rot90(m, k=k, axes=(0, 1))

    # 2. Change bits: under rotation, bits will be decoded differently
    def rot_num(x):
        d = (NUM2DIR[x] - k) % 4
        return DIR2NUM[d]

    m = np.vectorize(rot_num)(m)
    # 3. Convert back to bits
    return num_to_bits(m.astype(np.uint8))
