import argparse
import pathlib
import pprint
from typing import List
from PyPDF2 import PdfFileMerger, PdfFileReader


def build_book(pdf_files: List[pathlib.Path], output: pathlib.Path) -> pathlib.Path:
    merger = PdfFileMerger()
    for filename in pdf_files:
        merger.append(PdfFileReader(open(filename, "rb")))
    merger.write(output.as_posix())
    return output


def source_pdf_files(folder: pathlib.Path,
                     wildcard: str = "*.pdf") -> List[pathlib.Path]:
    if not folder.exists():
        raise ValueError("folder {folder} does not exist")
    files = list(folder.rglob(wildcard))
    if not files:
        raise ValueError(f"no pdf files maching '{wildcard}' in {folder}")
    return files


def parse_args(args: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="build playbook")
    parser.add_argument("folder", type=pathlib.Path, help="song folder")
    parser.add_argument(
        "output", type=pathlib.Path, help="output pdf file for the book"
    )
    parser.add_argument(
        "-n",
        "--negate",
        dest="negate",
        const=True,
        default=False,
        action="store_const",
        help="function call does nothing",
    )
    parser.add_argument(
        "-p",
        "--pattern",
        dest="pattern",
        default="*.pdf",
        help="wildcard pattern to select song files",
    )
    args = parser.parse_args(args)
    return args


def main(args=None):
    """build playbook"""
    import sys

    if not args:
        args = sys.argv[1:]
    args = parse_args(args)

    try:
        pdf_files = source_pdf_files(args.folder, args.pattern)
    except ValueError as err:
        print(err)
        sys.exit(1)

    pprint.pprint(pdf_files)

    if args.negate:
        sys.exit(0)
    else:
        build_book(sorted(pdf_files), args.output)


if __name__ == "__main__":
    main()
