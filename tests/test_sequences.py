import numpy as np
import pytest

from neuraldot import sequences


def test_sequence_lengths():
    assert len(sequences.MNS) == 63
    assert len(sequences.A1) == 236
    assert len(sequences.A2) == 233
    assert len(sequences.A3) == 31
    assert len(sequences.A4) == 241


@pytest.mark.parametrize(
    "seq,n,L",
    [
        (sequences.MNS, 6, 63),
        (sequences.A1, 5, 236),
        (sequences.A2, 5, 233),
        (sequences.A3, 5, 31),
        (sequences.A4_alt, 5, 241),
    ],
)
def test_sequence_quasi_debruijn(seq, n, L):
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

    assert len(set(hashes)) == L
