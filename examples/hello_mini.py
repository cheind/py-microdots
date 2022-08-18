def main():
    # Import the library
    import microdots as mdots

    from microdots.mini_sequences import MNS, A1, A2

    codec4x4 = mdots.AnotoCodec(
        mns=MNS,
        mns_order=4,
        sns=[A1, A2],
        pfactors=(3, 5),
        delta_range=(1, 15),
    )

    print(len(MNS), len(A1), len(A2))


main()
