def main():
    # Import the library
    import microdots as mdots

    # Use the default embodiment with A4 sequence fixed
    codec = mdots.anoto_6x6_a4_fixed

    # Generate a bit-matrix for section (10,2)
    G = codec.encode_bitmatrix(shape=(9, 16), section=(10, 2))

    # Render dots
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    mdots.draw_dots(G, grid_size=1.0, show_grid=True, ax=ax)
    fig.savefig("dots.pdf")
    plt.close(fig)

    # Decode a partial matrix
    S = G[3 : 3 + 6, 7 : 7 + 6]

    pos = codec.decode_position(S)
    sec = codec.decode_section(S, pos=pos)

    # To decode the rotation, use an extended matrix
    R = G[3 : 3 + 8, 7 : 7 + 8]
    rot = codec.decode_rotation(R)
    print("pos:", pos, "sec:", sec, "rot:", rot)
    # > pos: (7, 3) sec: (10, 2) rot: 0


main()
