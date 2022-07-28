import numpy as np
import pandas as pd
from neuraldot import integer


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


generate_numbers_pfactor_basis()
