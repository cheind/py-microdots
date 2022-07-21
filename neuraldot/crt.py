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
