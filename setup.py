"""Kata 13 - fizzbuzz als installierbares Programm.

Das Programm kann mit folgenden Befehlen installiert oder erstellt
werden:

Release in Unterordner erstellen: 
$ python3 setup.py sdist

Installation:
$ python3 setup.py install

Lokale Installation:
$ python3 setup.py install --user

"""

from setuptools import setup, find_packages

setup(
    name = "fizzbuzz_katas",
    version = "0.1",
    description = "Exercises with the famous FizzBuzz-Game.",
    packages = find_packages()
)

