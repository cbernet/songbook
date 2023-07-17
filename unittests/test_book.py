import os
import pathlib
import pytest
import tempfile

from songbook.book import source_pdf_files, build_book
from songbook.locate import abspath_data


def test_source_pdf_files():
    the_files = source_pdf_files(abspath_data("dummy_songbook"))
    assert len(the_files) == 4
    for f in the_files:
        assert f.exists()
        assert f.suffix == ".pdf"


def test_source_pdf_files_no_file():
    with pytest.raises(ValueError):
        _ = source_pdf_files(abspath_data("foo"))
    with pytest.raises(ValueError):
        _ = source_pdf_files(abspath_data("nosong"))
    with pytest.raises(ValueError):
        _ = source_pdf_files(abspath_data("dummy_songbook"), "*.foo")


@pytest.fixture
def output():
    out = pathlib.Path("book.pdf")
    yield out
    out.unlink()


def test_build_book(output):
    the_files = source_pdf_files(abspath_data("songbook"))
    output = build_book(the_files, output)
    assert output.exists()
