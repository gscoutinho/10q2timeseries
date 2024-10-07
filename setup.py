# setup.py

from setuptools import setup, find_packages

setup(
    name='sec_10q_etl',
    version='0.1.0',
    description='A package to transform SEC 10-Q data into DataFrames',
    author='Gabriel Coutinho',
    author_email='eng.gabrielcoutinho@outlook.com.br',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sec_10q_data',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose appropriate license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
