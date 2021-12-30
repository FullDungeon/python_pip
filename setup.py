import os

from setuptools import setup

with open('readme.md', 'r', encoding='utf-8') as file:
    readme = file.read()

setup(
    name='python pip template',                            # название пакета
    version='2021.12.30.0',
    author='FullDungeon',
    author_email='ddd.dungeon@gmail.com',
    description='Пакет для управления проектами',          # краткое описание
    long_description=readme,                               # полное опсиание (файл readme.md)
    url='https://github.com/FullDungeon/python_pip',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['colorama'],
    packages=['python_pip_template'],
    entry_points={                                         # точка входа
        'console_scripts': [
            'python-pip-template = python_pip_template.cmd:run',
        ],
    },
)