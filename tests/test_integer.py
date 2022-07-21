import numpy as np
from neuraldot.integer import NumberBasis


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
