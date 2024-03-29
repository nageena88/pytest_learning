#!/usr/bin/env python

from setuptools import setup, find_packages

long_description = """
This project is an example of a pytest
project featuring assertions,
exceptions, parametrization,
fixtures and factory fixtures.
"""

version = "1.0.0"

requirements = []

if __name__ == "__main__":
    setup(
        name="pytest_learning",
        version=version,
        description="Pytest Configuration Example",
        long_description=long_description,
        author="Ram Chauhan",
        packages=find_packages(
            exclude=[
                "tests",
            ],
            include=["scripts", "utils"],
        ),
        license="None",
        install_requires=requirements,
        classifiers=[
            "Development Status :: 1 - Planning",
            "Framework :: Pytest",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development",
            "Topic :: Software Development :: Libraries",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    )
