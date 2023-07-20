from setuptools import setup

setup(
    name="types-arpeggio",
    version="0.0.1.3-dev",
    packages=["arpeggio-stubs"],
    package_data={
        "arpeggio-stubs": ["*.pyi"],
    },
    install_requires=[
        "arpeggio>=1.3",
    ],
)
