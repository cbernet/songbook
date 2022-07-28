import pathlib
import songbook


def abspath_root():
    return pathlib.Path(songbook.__file__).parents[1]


def abspath_data(path):
    return abspath_root() / f"unittests/data/{path}"
