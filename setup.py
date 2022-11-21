#! /usr/bin/env python

"""Genetic Programming in Python, with a scikit-learn inspired API"""

from setuptools import find_packages, setup

import gplearn_torch

DESCRIPTION = __doc__
VERSION = gplearn_torch.__version__

setup(
    name="gplearn_torch",
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    author="S P Sharan",
    author_email="spsharan2000@gmail.com",
    url="https://github.com/Syzygianinfern0/gplearn-torch",
    license="new BSD",
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    zip_safe=False,
    package_data={"": ["LICENSE"]},
    install_requires=["scikit-learn>=1.0.2", "joblib>=1.0.0", "torch>=1.13.0", "numpy>=1.23.4"],
)
