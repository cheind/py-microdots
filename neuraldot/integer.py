"""This is just a demo script that shows how to reconstruct numbers in
a specific range from bases, coefficients relating to their prime factors"""

import numpy as np


class NumberBasis:
    def __init__(self, pfactors: np.ndarray):
        """Initialize basis from prime-factors.

        Given prime-factors p1,...,pn the integer interval [0,p1*...*pn)
        can be represented uniquely using n coefficients (one for each basis).
        The n-th basis is given by p1*...*p(n-1). The first basis is 1.
        The coeffiences for the i-th basis are in the range [0,pi).

        Note, the order of the p1,...,pn gives raise to different bases
        and hence different coefficient representations for the same integer.
        """
        self.upper = np.prod(pfactors)
        self.lower = 0
        p = np.concatenate([[1], pfactors])
        p = np.cumprod(p)
        self.bases = p[:-1]
        self.rbases = self.bases[::-1]

    def project(self, n: np.ndarray) -> np.ndarray:
        """Returns coefficents for prime bases for each number.

        Params:
            n: (M,) array of numbers >=0 and less than product
                of prime-factors.

        Returns:
            coeffs: (M,B) array of coefficients for each number
                and each basis.
        """
        n = np.asarray(n)
        assert np.logical_and(n >= 0, n < self.upper).all()
        coeffs = []
        for b in self.rbases:
            coeffs.append(n // b)
            n = n % b
        return np.array(coeffs[::-1], dtype=n.dtype).T

    def reconstruct(self, coeffs: np.ndarray) -> np.ndarray:
        """Reconstruct integers from coefficients.

        Each number x can be represented as
            x = b1*c1 + b2*c2 + ... + bn*cn,
        which we can rewrite as the inner product
            <[b1,...,bn],[c1,...,cn]>.
        For multiple sets of coefficients this turns into a matrix
        multiplication between coeffs (M,B) and bases (B,1).

        Params:
            coeffs: (M,B) matrix of B coefficients for M integers.

        Returns:
            nums: (M,) array of reconstructed integers.

        """
        return np.squeeze(coeffs @ self.bases[:, np.newaxis], -1)
