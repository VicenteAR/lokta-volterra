"""lokta_volterra package installation metadata."""
from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import find_packages, setup


version = SourceFileLoader(
    "lokta_volterra.version",
    str(Path(__file__).parent / "lokta_volterra" / "version.py"),
).load_module()

with open(Path(__file__).with_name("README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="lokta_volterra",
    description="Lokta-Volterra model of species competition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    version=version.__version__,
    license="MIT",
    author="VicenteAR",
    author_email="",
    url="",
    keywords=["Machine learning", "artificial intelligence"],
    tests_require=["pytest>=5.3.5", "hypothesis>=5.6.0"],
    extras_require={},
    install_requires=[],
    package_data={"": ["README.md"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
    ],
)
