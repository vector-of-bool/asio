import argparse
from pathlib import Path
from typing import Sequence
import subprocess
import sys
import shutil


THIS_SCRIPT = Path(__file__).absolute().resolve()
ROOT = THIS_SCRIPT.parent
ASIO_DIR = ROOT / 'asio'
ASIO_SRC = ASIO_DIR / 'src'
ASIO_INC = ASIO_DIR / 'include'

DEST_ROOT = ROOT
DEST_SRC = DEST_ROOT / 'src'
DEST_INC = DEST_ROOT / 'include'


def main(argv: Sequence[str]) -> None:
    parser = argparse.ArgumentParser()
    args = parser.parse_args(argv)
    shutil.rmtree(DEST_SRC, ignore_errors=True)
    shutil.rmtree(DEST_INC, ignore_errors=True)

    shutil.copytree(ASIO_SRC, DEST_SRC)
    shutil.copytree(ASIO_INC, DEST_INC)

    shutil.rmtree(DEST_SRC / 'examples')
    shutil.rmtree(DEST_SRC / 'tests')
    shutil.rmtree(DEST_SRC / 'doc')


if __name__ == "__main__":
    main(sys.argv[1:])
