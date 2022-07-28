import matplotlib.pyplot as plt
from neuraldot.defaults import anoto_encoder_6x6_a4_fixed
from neuraldot.draw import draw_dots


def generate_pattern_plot():
    bits = anoto_encoder_6x6_a4_fixed.encode_bitmatrix((6, 16), section=(0, 0))
    fig, ax = plt.subplots(figsize=plt.figaspect(6 / 16))
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params("x", labelsize=12)
    ax.tick_params("y", labelsize=12)

    draw_dots(bits, dot_scale=40, ax=ax)
    fig.tight_layout()
    fig.savefig("doc/anoto_pattern.pdf")
    plt.show()


generate_pattern_plot()
