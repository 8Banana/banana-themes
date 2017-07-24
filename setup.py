#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name="banana-themes",
    description="Themes by the 8banana team",
    keywords="",
    url="https://github.com/8Banana/banana-themes",
    author="8Banana",
    version="1.0.0",
    copyright="Copyright (c) 2017 8Banana",
    license="MIT",

    install_requires=["pygments"],
    packages=find_packages(),
    entry_points = {
        "pygments.styles": ["zaab = banana_themes:Zaab",
                            "hitgub = banana_themes:HitGub"],
    },
)
