import numpy as np
from neuraldot.integer import NumberBasis, CRT


def test_numberbasis():
    nb = NumberBasis([3, 3, 2, 3])
    coeffs = nb.project(np.arange(nb.upper))
    assert coeffs.shape == (54, 4)
    assert all(nb.reconstruct(coeffs) == np.arange(54))

    # Permutations of prime-factors gives different set
    # of coefficients but represents the same number range.
    nb = NumberBasis([2, 3, 3, 3])
    coeffs2 = nb.project(np.arange(nb.upper))
    assert coeffs2.shape == (54, 4)
    assert (coeffs2 != coeffs).any()
    assert all(nb.reconstruct(coeffs2) == np.arange(54))


def test_crt():
    crt = CRT([3, 4, 5])
    assert crt.solve([0, 3, 4]) == 39

    crt = CRT([236, 233, 31, 241])
    assert all(crt.qs == [135, 145, 17, 62])
    # Each ei is 1 for li and 0 for all other lengths
    assert all(np.remainder(crt.es, crt.lengths[0]) == [1, 0, 0, 0])
    assert all(np.remainder(crt.es, crt.lengths[1]) == [0, 1, 0, 0])
    assert all(np.remainder(crt.es, crt.lengths[2]) == [0, 0, 1, 0])
    assert all(np.remainder(crt.es, crt.lengths[3]) == [0, 0, 0, 1])

    # TODO: the patent contains an example that
    # yields 170326961 for remainders [97,176,3,211]
    # but that's not correct. Instead
    assert crt.solve([97, 0, 3, 211]) == 170326961

    assert crt.solve([0, 0, 0, 0]) == 0
