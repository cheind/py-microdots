import matplotlib.pyplot as plt
import matplotlib.patches as P
from neuraldot.defaults import anoto_6x6_a4_fixed, anoto_6x6
from neuraldot.draw import draw_dots


def generate_pattern_plot():
    bits = anoto_6x6.encode_bitmatrix((8, 16), section=(0, 0))
    fig, ax = plt.subplots(figsize=plt.figaspect(8 / 16))

    draw_dots(bits, dot_scale=25, ax=ax)

    ax.add_patch(
        P.Rectangle(
            (2 - 0.5, 1 - 0.5),
            6,
            6,
            fill=False,
            edgecolor="green",
            zorder=3,
            linewidth=2,
        )
    )
    ax.add_patch(
        P.Rectangle(
            (7 - 0.5, 2 - 0.5),
            6,
            6,
            fill=False,
            edgecolor="purple",
            zorder=3,
            linewidth=2,
        )
    )
    ax.annotate("(2,1)", (2 - 0.3, 1 - 0.15), color="green", fontsize=11)
    ax.annotate("(7,2)", (7 - 0.3, 2 - 0.15), color="purple", fontsize=11)

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.tick_params("x", labelsize=12)
    ax.tick_params("y", labelsize=12)
    ax.grid(which="major", alpha=0.4, linestyle="--", color="gray", zorder=0)
    fig.tight_layout()
    fig.savefig("doc/anoto_pattern.pdf")
    plt.show()


generate_pattern_plot()
