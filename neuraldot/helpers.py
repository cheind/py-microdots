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


def rot90_cw(bitmatrix: np.ndarray) -> np.ndarray:
    """Simulates a 90° clockwise rotation of the bitmatrix."""
    m = bits_to_num(bitmatrix)
    # 1. Rotate array
    m = np.rot90(m, k=1, axes=(1, 0))
    # 2. Change bits: a north displacement, will turn to an east etc.
    dir_map = [2, 0, 3, 1]

    def map_num(x):
        return dir_map[x]

    m = np.vectorize(map_num)(m)
    # 3. Convert back to bits
    return num_to_bits(m.astype(np.uint8))
