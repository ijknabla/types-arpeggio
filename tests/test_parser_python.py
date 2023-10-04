from __future__ import annotations

import sys
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any

import pytest
from arpeggio import DEFAULT_WS, EOF, ParserPython, Sequence

from . import DefaultAndValues, iter_kw_args, iter_pos_args

if TYPE_CHECKING:
    from arpeggio import _ParsingExpressionLike, _SyntaxClasses


def empty() -> _ParsingExpressionLike:
    return EOF


comment_def_values = DefaultAndValues["_ParsingExpressionLike | None"](
    None, [empty]
)
syntax_classes_values = DefaultAndValues["_SyntaxClasses"](
    {}, [{"Sequence": Sequence}]
)

skipws_values = DefaultAndValues[bool](True, [False])
ws_values = DefaultAndValues[str](DEFAULT_WS, ["\u3000"])

reduce_tree_values = (
    autokwd_values
) = ignore_case_values = memoization_values = DefaultAndValues[bool](
    False, [True]
)

debug_values = DefaultAndValues[bool](False, [True])
file_values = DefaultAndValues[IO[str]](sys.stdout, [sys.stderr])


@pytest.mark.parametrize(
    "kwargs,"
    "comment_def,"
    "syntax_classes,"
    "skipws,"
    "ws,"
    "reduce_tree,"
    "autokwd,"
    "ignore_case,"
    "memoization,"
    "debug,"
    "file,",
    iter_kw_args(
        comment_def=comment_def_values,
        syntax_classes=syntax_classes_values,
        skipws=skipws_values,
        ws=ws_values,
        reduce_tree=reduce_tree_values,
        autokwd=autokwd_values,
        ignore_case=ignore_case_values,
        memoization=memoization_values,
        debug=debug_values,
        file=file_values,
    ),
)
def test_parser_python_keyword_arguments(
    tempdir: Path,
    kwargs: dict[str, Any],
    comment_def: _ParsingExpressionLike | None,
    syntax_classes: _SyntaxClasses,
    skipws: bool,
    ws: str,
    reduce_tree: bool,
    autokwd: bool,
    ignore_case: bool,
    memoization: bool,
    debug: bool,
    file: IO[str],
) -> None:
    parser = ParserPython(empty, **kwargs)
    assert (parser.comments_model is None) == (comment_def is None)
    assert parser.syntax_classes == syntax_classes
    assert parser.skipws == skipws
    assert parser.ws == ws
    assert parser.reduce_tree == reduce_tree
    assert parser.autokwd == autokwd
    assert parser.ignore_case == ignore_case
    assert parser.memoization == memoization
    assert parser.debug == debug
    assert parser.file == file


@pytest.mark.parametrize(
    "args,"
    "comment_def,"
    "syntax_classes,"
    "skipws,"
    "ws,"
    "reduce_tree,"
    "autokwd,"
    "ignore_case,"
    "memoization,",
    iter_pos_args(
        comment_def_values,
        syntax_classes_values,
        skipws_values,
        ws_values,
        reduce_tree_values,
        autokwd_values,
        ignore_case_values,
        memoization_values,
    ),
)
@pytest.mark.parametrize(
    "kwargs," "debug," "file,",
    iter_kw_args(
        debug=debug_values,
        file=file_values,
    ),
)
def test_parser_python_positional_arguments(
    tempdir: Path,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
    comment_def: _ParsingExpressionLike | None,
    syntax_classes: _SyntaxClasses,
    skipws: bool,
    ws: str,
    reduce_tree: bool,
    autokwd: bool,
    ignore_case: bool,
    memoization: bool,
    debug: bool,
    file: IO[str],
) -> None:
    parser = ParserPython(empty, *args, **kwargs)
    assert (parser.comments_model is None) == (comment_def is None)
    assert parser.syntax_classes == syntax_classes
    assert parser.skipws == skipws
    assert parser.ws == ws
    assert parser.reduce_tree == reduce_tree
    assert parser.autokwd == autokwd
    assert parser.ignore_case == ignore_case
    assert parser.memoization == memoization
    assert parser.debug == debug
    assert parser.file == file
