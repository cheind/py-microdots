def main():
    # Import the library
    import microdots as mdots
    import matplotlib.pyplot as plt

    # Use the default embodiment with A4 sequence fixed
    codec = mdots.anoto_6x6_a4_fixed

    # Generate a bit-matrix for section (10,2)
    bits = codec.encode_bitmatrix(shape=(9, 16), section=(10, 2))

    # Decode a partial matrix
    pos = codec.decode_location(bits[3:, 7:])
    sec = codec.decode_section(bits[3:, 7:], pos=pos)
    rot = codec.decode_rotation(bits[3:, 7:])
    print("pos:", pos, "sec:", sec, "rot:", rot)
    # > pos: (7, 3) sec: (10, 2) rot: 0

    # Render dots
    fig, ax = plt.subplots()
    mdots.draw_dots(bits, grid_size=1.0, show_grid=True, ax=ax)
    fig.savefig("dots.pdf")
    plt.close(fig)


main()
