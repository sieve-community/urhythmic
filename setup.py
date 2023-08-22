import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="urhythmic",
    py_modules=["urhythmic"],
    version="0.1",
    description="Urhythmic: Rhythm Modeling for Voice Conversion",
    readme="README.md",
    python_requires=">=3.9",
    author="Benjamin van Niekerk",
    url="https://github.com/bshall/urhythmic",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
