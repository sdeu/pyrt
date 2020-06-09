import codecs
import os

from setuptools import setup, find_packages


###################################################################

NAME = "pyrtrender"
PACKAGES = find_packages(where="src")

###################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


if __name__ == "__main__":
    setup(
        name=NAME,
        packages=PACKAGES,
        package_dir={"": "src"},
        options={"bdist_wheel": {"universal": "1"}},
    )