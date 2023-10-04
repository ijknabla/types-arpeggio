from __future__ import annotations

from typing import TYPE_CHECKING

from arpeggio import EOF, ParserPython

if TYPE_CHECKING:
    from arpeggio import _ParsingExpressionLike


def empty() -> _ParsingExpressionLike:
    return EOF


def test_parser_python_init() -> None:
    ParserPython(empty)
