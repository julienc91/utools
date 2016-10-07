# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="utools",
    version="1.3",
    author="Julien Chaumont",
    author_email="utools@julienc.io",
    description="A set of useful functions to use for various purposes in any Python project",
    license="MIT",
    url="http://github.com/julienc91/utools/",
    packages=find_packages(),
    install_requires=["typing"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]
)
