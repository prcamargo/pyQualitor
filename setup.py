# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pyQualitor',
    version='0.0.1',
    url='https://github.com/paulor1610/pyQualitor',
    license='MIT License',
    author='Paulo Roberto',
    author_email='paulor1610@gmail.com',
    keywords='API Qualitor',
    description='API Qualitor Python',
    packages=find_packages(),
    install_requires=['zeep>=3.4'],
    long_description='API Qualitor em python utilizando o Web Service'
)