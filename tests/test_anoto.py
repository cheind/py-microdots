import numpy as np
import pytest

from neuraldot import anoto


def test_sequence_lengths():
    assert len(anoto.MNS) == 63
    assert len(anoto.A1) == 236
    assert len(anoto.A2) == 233
    assert len(anoto.A3) == 31
    assert len(anoto.A4) == 241


@pytest.mark.parametrize(
    "seq,n,L",
    [
        (anoto.MNS, 6, 63),
        (anoto.A1, 5, 236),
        (anoto.A2, 5, 233),
        (anoto.A3, 5, 31),
        # (anoto.A4, 5, 241),
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


def test_bitmatrix_encode_different_sections():
    an = anoto.Anoto()

    m = an.encode_bitmatrix((60, 60), section=(0, 0))
    assert m.shape == (60, 60, 2)
    assert np.all(m[:8, 0, 0] == (0, 0, 0, 0, 0, 0, 1, 0))
    assert np.all(m[0, :8, 1] == (0, 0, 0, 0, 0, 0, 1, 0))

    m = an.encode_bitmatrix((60, 60), section=(1, 1))
    assert m.shape == (60, 60, 2)
    assert np.all(m[:8, 0, 0] == (0, 0, 0, 0, 0, 1, 0, 0))
    assert np.all(m[0, :8, 1] == (0, 0, 0, 0, 0, 1, 0, 0))


@pytest.mark.parametrize(
    "size,section",
    [
        (600, (0, 0)),
        # (600, (10, 10)),
    ],
)
def test_bitmatrix_encode_decode(size, section):
    an = anoto.Anoto()

    m = an.encode_bitmatrix((size, size), section=section)
    assert m.shape == (size, size, 2)

    xy = an.decode_bitmatrix(m[0:, 217:])
    print(xy)

    # for y in range(size - 6):
    #     for x in range(size - 6):
    #         xy = an.decode_bitmatrix(m[y : y + 6, x : x + 6])
    #         print(xy, (x, y))
    #         assert xy == (x, y)
