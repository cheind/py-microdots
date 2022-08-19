import pandas as pd
import timeit
import microdots as mdots
from functools import partial


codec = mdots.anoto_6x6_a4_fixed


def encode_test():
    #  A0 841 x 1188 @ 0.3mm
    return codec.encode_bitmatrix(
        shape=(int(1188 * 0.3), int(841 * 0.3)), section=(10, 2)
    )


G = encode_test()


def decode_position(P):
    return codec.decode_position(P)


def decode_section(P, pos):
    return codec.decode_section(P, pos=pos)


def decode_rotation(P):
    return codec.decode_rotation(P)


def main():
    N = 100
    data = {
        "Encoding": timeit.Timer(
            "encode_test()", "from __main__ import encode_test"
        ).timeit(number=N)
        / N,
        "Decode position": timeit.Timer(
            "decode_position(G[100:, 100:])", "from __main__ import decode_position, G"
        ).timeit(number=N)
        / N,
        "Decode section": timeit.Timer(
            "decode_section(G[100:, 100:],pos=(100,100))",
            "from __main__ import decode_section, G",
        ).timeit(number=N)
        / N,
        "Decode rotation": timeit.Timer(
            "decode_rotation(G[100:100+8, 100::100+8])",
            "from __main__ import decode_rotation, G",
        ).timeit(number=N)
        / N,
    }
    print(data)

    data = [
        (k, r"$\SI{" + str(int(v * 1e6)) + r"}{\micro\second}$")
        for k, v in data.items()
    ]
    df = pd.DataFrame(data, columns=["Task", "Time"])
    df = df.set_index("Task")
    print(df.to_latex(escape=False))


main()
