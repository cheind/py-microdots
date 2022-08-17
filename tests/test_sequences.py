import numpy as np
import pytest

from microdots import anoto_sequences, mini_sequences


@pytest.mark.parametrize(
    "seq,n,L,isdebruijn",
    [
        (anoto_sequences.MNS, 6, 63, True),
        (anoto_sequences.A1, 5, 236, True),
        (anoto_sequences.A2, 5, 233, True),
        (anoto_sequences.A3, 5, 31, True),
        (anoto_sequences.A4_alt, 5, 241, True),
        (anoto_sequences.A4, 5, 241, False),
        (mini_sequences.MNS, 4, 16, True),
        (mini_sequences.A1, 3, 27, True),
        (mini_sequences.A2, 3, 125, True),
    ],
)
def test_sequence_quasi_debruijn(seq, n, L, isdebruijn):
    # make it cyclic
    cseq = np.concatenate((seq, seq[: (n - 1)]))
    view = np.lib.stride_tricks.sliding_window_view(cseq, n, axis=0)
    assert view.shape == (L, n)
    hashes = np.apply_along_axis(lambda w: hash(w.tobytes()), 1, view)

    s = {}
    for idx, (e, h) in enumerate(zip(view, hashes)):
        if h in s:
            print("collision")
            print(idx, h, s[h], e)
        else:
            s[h] = (e, idx)

    num_unique = len(set(hashes))

    assert num_unique == L if isdebruijn else num_unique < L
