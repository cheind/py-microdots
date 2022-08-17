from setuptools import setup, find_packages
from pathlib import Path

THISDIR = Path(__file__).parent


def read_requirements(fname):
    with open(THISDIR / "requirements" / fname, "r") as f:
        return f.read().splitlines()


core_required = read_requirements("requirements.txt")
dev_required = read_requirements("dev-requirements.txt") + core_required

main_ns = {}
with open(THISDIR / "microdots" / "__version__.py") as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name="microdots",
    version=main_ns["__version__"],
    description="A modern Python library to encode/decode with Anoto dot patterns.",
    author="Christoph Heindl",
    url="https://github.com/cheind/py-microdots",
    license="MIT",
    install_requires=core_required,
    packages=find_packages(".", include="microdots*"),
    include_package_data=True,
    keywords="speckle pattern coding anoto dot encode decode",
    extras_require={
        "dev": dev_required,
    },
)
