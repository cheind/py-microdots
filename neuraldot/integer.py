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
                and each basis, starting with the b1.
        """
        n = np.asarray(n)
        assert np.logical_and(n >= 0, n < self.upper).all()
        coeffs = []
        for b in self.rbases:
            q, r = np.divmod(n, b)
            coeffs.append(q)
            n = r
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


def extended_euclid(a, b):
    """Returns GCD and r,s such that gcd=r*a+s*b.

    This is algorithm is used to find s such that
    1 = r*a+s*b where a and b are relatively prime.
    """
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_euclid(b % a, a)

    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


class CRT:
    """Solves for simulatenous congruences using the Chinese Remainder Theorem (CRT).

    ## Method
    Assume that l1,...,ln are relatively prime, then according to the CRT
    a natural number x exists such that for each tuple a1,...,an
        x == ai (mod li)
    holds. Here ai are the remainders and == means congruent.

    The method used below finds x by constructing x as a sum of factors with
    the property that if we hit x with mod li, all but the i-th term will
    vanish and x (mod li) can be written as
        x (mod li) = [0 + ... + ai (mod li) + 0 ... + 0] (mod li) = ai (mod li)
    as desired.

    We proceed as follows. We know that [1] for any integers c,d two integers
    r, s exist such that
        gcd(c,d) = r*c + s*d.
    if c,d are relatively prime we have
        1=r*c + s*d.
    Let ci=li and di=l1*...*ln/li. Since all li are pairwise relatively prime,
    ci and di are relatively prime. Therefore,
        1=ri*li + si*l1*...*ln/li
    Apply mod li and distribute we get
        1 (mod li) = ri*li (mod li) + si*l1*...*ln/li (mod li).
    Since ri*li (mod li) = 0, we know that
        1 = si*l1*...*ln/li (mod li)
    Denote ei = si*l1*...*ln/li and find x as
        x = e1*a1+...+en*an,
    which has the desired property that
        x (mod li)  = [0+...0+ei*ai (mod li)+0...+0] (mod li)
                    = [ei (mod li) * ai (mod li)] (mod li)
                    = [1 * ai (mod li)] (mod li)
                    = ai (mod li).

    See:
    [1] https://mathworld.wolfram.com/GreatestCommonDivisorTheorem.html
    https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    https://de.wikipedia.org/wiki/Chinesischer_Restsatz#Finden_einer_L%C3%B6sung
    """

    def __init__(self, lengths: list[int]) -> None:
        self.lengths = np.asarray(lengths)
        self.L = np.prod(self.lengths)
        self.qs = self._compute_qs(self.lengths)
        self.es = self.qs * (self.L // self.lengths)

    def solve(self, remainders: list[int]) -> int:
        """Returns the smallest positive number solving the remainder congruences.

        Params:
            remainders: list of remainders, ri, such that ri = x mod li where
                li is the i-th list length.
        """
        # We make use of
        #     a + b = c => a (mod N) + b (mod N) = c (mod N)
        # to avoid having large addition terms.
        return np.sum((remainders * self.es) % self.L) % self.L

    def _compute_qs(self, lengths: list[int]) -> list[int]:
        L = np.prod(lengths)
        qs = []
        for li in lengths:
            gcd, _, s = extended_euclid(li, L // li)
            if not gcd == 1:
                raise ValueError("List lengths must be relatively prime.")
            # Take closest positive s (doesn't change CRT algorithm)
            s = s % li
            qs.append(s)
        return np.array(qs)


if __name__ == "__main__":

    crt = CRT([236, 233, 31, 241])
    print(crt.qs)
    print(crt.solve([97, 176, 3, 2]))
