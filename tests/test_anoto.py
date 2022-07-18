from neuraldot import anoto


def test_sequence_lengths():
    assert len(anoto.MNS) == 63
    assert len(anoto.A1) == 236
    assert len(anoto.A2) == 233
    assert len(anoto.A3) == 31
    assert len(anoto.A4) == 241
