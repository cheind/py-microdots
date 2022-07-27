from .anoto_sequences import MNS, A1, A2, A3, A4, A4_alt
from .codec import AnotoEncoder, AnotoDecoder


anoto_encoder_6x6 = AnotoEncoder(
    mns=MNS,
    mns_order=6,
    sns=(A1, A2, A3, A4),
    pfactors=[3, 3, 2, 3],
    delta_range=(5, 58),
)

anoto_encoder_6x6_a4_fixed = AnotoEncoder(
    mns=MNS,
    mns_order=6,
    sns=(A1, A2, A3, A4_alt),
    pfactors=[3, 3, 2, 3],
    delta_range=(5, 58),
)

anoto_decoder_6x6 = AnotoDecoder(
    mns=MNS,
    mns_order=6,
    sns=(A1, A2, A3, A4),
    pfactors=[3, 3, 2, 3],
    delta_range=(5, 58),
)

anoto_decoder_6x6_a4_fixed = AnotoDecoder(
    mns=MNS,
    mns_order=6,
    sns=(A1, A2, A3, A4_alt),
    pfactors=[3, 3, 2, 3],
    delta_range=(5, 58),
)
