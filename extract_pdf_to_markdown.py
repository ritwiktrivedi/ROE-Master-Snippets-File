import pymupdf4llm
import pathlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "file",
    help="name of the input file",
)
args = parser.parse_args()
md_text = pymupdf4llm.to_markdown(args.file)
pathlib.Path("output.md").write_bytes(md_text.encode())
