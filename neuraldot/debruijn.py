from typing import Iterable, Union, Any


def de_bruijn(k: Union[Iterable[Any], int], n: int) -> str:
    """de Bruijn sequence for alphabet k and subsequences of length n.

    Taken from
    https://en.wikipedia.org/wiki/De_Bruijn_sequence
    """
    # Two kinds of alphabet input: an integer expands
    # to a list of integers as the alphabet..
    if isinstance(k, int):
        alphabet = list(map(str, range(k)))
    else:
        # While any sort of list becomes used as it is
        alphabet = k
        k = len(k)

    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                sequence.extend(a[1 : p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return "".join(alphabet[i] for i in sequence)


if __name__ == "__main__":
    import numpy as np

    s = np.array([int(c) for c in de_bruijn(3, 5)])
    print(len(s))
    print(repr(s))

    msg = "0000222202221022200221202211022100220002122021210212002112021110211002100020220202102020020100200001222012210122001212012110121001200011220112101120011120111122221222112211121221212112111110111001100010220102101020010120201201011020110101001"
    s = np.array([int(c) for c in msg])
    print(len(s))
    print(repr(s))
