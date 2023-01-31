from setuptools import setup

setup(
    name="types-arpeggio",
    version="0.0.0",
    packages=["arpeggio-stubs"],
    package_data={
        "arpeggio-stubs": ["*.pyi"],
    },
    install_requires=[
        "arpeggio>=0.8",
    ],
)
