import numpy as np


def draw_dots(
    bitmatrix: np.ndarray,
    offset_lut: np.ndarray = None,
    grid_size: float = 1.0,
    dot_scale: float = 10.0,
    show_grid: bool = True,
    set_ax_props: bool = True,
    ax=None,
):
    """Draw the dot pattern.

    This method draws the dot pattern for visual purposes and is not meant for
    printing onto surfaces.

    Params:
        bitmatrix: (M,N,2) or (M,N) matrix of bits to draw. If three dimensional,
            layout is assumed to be M rows, N columns and each element contains 2 bits
            one for x and one for y. Otherwise, each cell is assumed to contain
            a value in the range [0,3].
        offset_lut: optional (4,2) matrix indicating for each number in [0,3] an
            dot offset direction. If not given a default one is assumed.
        grid_size: nominal distance between two grid lines.
        show_grid: If True, also shows the nominal grid lines.
        set_ax_props: If True, sets default axis properties.
        ax: When given uses this axis, otherwise gca().
    """
    if bitmatrix.ndim == 3:
        # Little order: x is lowest bit, y is highes bit => 10 = 2 means x=0,y=1
        bitmatrix = np.packbits(bitmatrix, axis=-1, bitorder="little").squeeze(-1)

    # Taken from
    # https://patentimages.storage.googleapis.com/b8/ef/c2/046cdc9e044b9e/US7999798.pdf
    if offset_lut is None:
        offset_lut = np.array(
            [
                [0, -1.0],  # 0: north
                [1.0, 0.0],  # 1: east
                [-1.0, 0.0],  # 2: west
                [0.0, 1.0],  # 3: south
            ]
        )
    offset_scale = grid_size * 1 / 6

    if ax is None:
        ax = plt.gca()

    offsets = offset_lut[bitmatrix] * offset_scale  # (M,N,2)
    dots = np.stack(
        np.meshgrid(
            range(bitmatrix.shape[1]), range(bitmatrix.shape[0]), indexing="xy"
        ),
        -1,
    )
    print(bitmatrix.shape)
    dots = dots + offsets
    ax.scatter(dots[..., 0], dots[..., 1], s=dot_scale, marker="o", color="k", zorder=2)

    if show_grid:
        ax.set_xticks(np.arange(dots.shape[1]) * grid_size)
        ax.set_yticks(np.arange(dots.shape[0]) * grid_size)
        ax.grid(which="major", alpha=0.4, linestyle="--", color="r", zorder=0)

    if set_ax_props:
        ax.invert_yaxis()  # top-left origin
        ax.set_aspect("equal")


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from .defaults import anoto_encoder_6x6_a4_fixed

    bits = anoto_encoder_6x6_a4_fixed.encode_bitmatrix((10, 10), section=(0, 0))
    print(bits[:3, :3])

    fig, ax = plt.subplots()

    draw_dots(bits, ax=ax)
    plt.show()
