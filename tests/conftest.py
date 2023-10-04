from __future__ import annotations

import os
from collections.abc import Generator
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


@pytest.fixture
def tempdir() -> Generator[Path, None, None]:
    with TemporaryDirectory() as directory:
        cwd = Path.cwd()
        os.chdir(directory)
        try:
            yield Path(directory)
        finally:
            os.chdir(cwd)
