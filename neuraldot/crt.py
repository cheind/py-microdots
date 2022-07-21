import numpy as np


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

    Assume that l1,...,ln are relatively prime, then according to the CRT
    a natural number x exists for each tuple a1,...,an such that
        x == ai (mod li),
    for given remainders ai and == meaning congruent.

    To find x, we make use of the property that
        gcd(c,d) = r*c + s*d.
    If additionaly c and d are relatively prime we have
        1 = r*c + s*d.
    Assume we let c=li and d=L/li, where L=l1*...*ln. Since l1,...,ln are
    relatively prime, li and L/li will also be relatively prime.
    Hence we know that e = s*(L/li) will be 1 (mod li) and 0 otherwise. We can
    find one such ei corresponding to each li.

    The smallest positive x is then found to be
        x = e1*a1+...+en*an (mod L)

    Note, by construction for x mod li, all but one (ei*ai) of the above terms
    vanishes. So, for x mod li we have ei*ai = ai as desired.

    See:
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
