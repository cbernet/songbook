import os

from chansons.locate import abspath_root, abspath_data


def test_root():
    root = abspath_root()
    elements = os.listdir(root)
    assert {"chansons", "unittests"}.issubset(elements)


def test_data():
    image = abspath_data("foo.txt")
    assert image.exists()
