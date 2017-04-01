"""
Kata 13 - fizzbuzz als installierbares Programm.
"""

from setuptools import setup, find_packages

setup(
    name = "fizzbuzz_katas",
    version = "0.1",
    description = "Exercises with the famous FizzBuzz-Game.",
    packages = find_packages()
)

# realease: python3 setup.py sdist
# install: python3 setup.py install
# install locally: python3 setup.py install --user
