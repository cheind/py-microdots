import numpy as np
import pandas as pd
from microdots import integer


def generate_numbers_pfactor_basis():
    nums = np.arange(12)
    perms = [[2, 2, 3], [2, 3, 2], [3, 2, 2]]

    data = {}

    for pf in perms:
        cname = f'[{",".join(str(p) for p in pf)}]'
        coeffs = integer.NumberBasis(pf).project(nums)
        str_coeffs = []
        for cs in coeffs:
            str_coeffs.append(f'{"".join([str(c) for c in cs])}')
        data[cname] = str_coeffs

    df = pd.DataFrame(data)
    print(df.to_latex())


def generate_tuples_relative_prime():
    data = {}
    data["$s_1=(2,6)$"] = [{f"$\\langle {i%2},{i%6} \\rangle$"} for i in range(12)]
    data["$s_2=(3,4)$"] = [{f"$\\langle {i%3},{i%4} \\rangle$"} for i in range(12)]

    df = pd.DataFrame(data)
    print(df.to_latex(escape=False))


def generate_symbol_lookup_table():
    data = {}
    data["Symbol"] = ["N(orth)", "E(ast)", "S(outh)", "W(est)"]
    data["$x$"] = [0, 0, 1, 1]
    data["$y$"] = [0, 1, 1, 0]

    df = pd.DataFrame(data)
    print(df.to_latex(escape=False))


generate_numbers_pfactor_basis()
generate_tuples_relative_prime()
generate_symbol_lookup_table()
