from __future__ import annotations

from collections.abc import Collection, Generator
from pathlib import Path
from typing import TYPE_CHECKING, Any

import pytest
from arpeggio import DEFAULT_WS, EOF, ParserPython, Sequence

from . import DefaultAndValues, iter_pos_args

if TYPE_CHECKING:
    from arpeggio import _ParsingExpressionLike, _SyntaxClasses


def optional_keyword_generator(
    *args: Collection[Any],
) -> Generator[tuple[Any | None, ...], None, None]:
    ndim = len(args)
    yield (None,) * ndim
    for i, collection in enumerate(args):
        for item in collection:
            yield tuple(item if j == i else None for j, _ in enumerate(args))


def empty() -> _ParsingExpressionLike:
    return EOF


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
        DefaultAndValues["_ParsingExpressionLike | None"](None, [empty]),
        DefaultAndValues["_SyntaxClasses | None"](
            {}, [{"Sequence": Sequence}]
        ),
        DefaultAndValues[bool](True, [False]),
        DefaultAndValues[str](DEFAULT_WS, ["\u3000"]),
        DefaultAndValues[bool](False, [True]),
        DefaultAndValues[bool](False, [True]),
        DefaultAndValues[bool](False, [True]),
        DefaultAndValues[bool](False, [True]),
    ),
)
def test_parser_python_positional_arguments(
    args: tuple[Any, ...],
    comment_def: _ParsingExpressionLike | None,
    syntax_classes: _SyntaxClasses | None,
    skipws: bool,
    ws: str | None,
    reduce_tree: bool,
    autokwd: bool,
    ignore_case: bool,
    memoization: bool,
) -> None:
    parser = ParserPython(empty, *args)
    assert (parser.comments_model is None) == (comment_def is None)
    assert parser.syntax_classes == syntax_classes
    assert parser.skipws == skipws
    assert parser.ws == ws
    assert parser.reduce_tree == reduce_tree
    assert parser.autokwd == autokwd
    assert parser.ignore_case == ignore_case
    assert parser.memoization == memoization


@pytest.mark.parametrize(
    """
    comment_def,
    syntax_classes,
    autokwd,
    debug,
    ignore_case,
    memoization,
    reduce_tree,
    skipws,
    ws,
    """,
    optional_keyword_generator(
        list["_ParsingExpressionLike"]([empty]),  # comment_def
        list["_SyntaxClasses"]([{}]),  # syntax_classes
        [True],  # autokwd
        [True],  # debug
        [True],  # ignore_case
        [True],  # memoization
        [True],  # reduce_tree,
        [True],  # skipws
        [""],  # ws
    ),
)
def test_parser_python_init(
    tempdir: Path,
    comment_def: _ParsingExpressionLike,
    syntax_classes: _SyntaxClasses,
    autokwd: bool,
    debug: bool,
    ignore_case: bool,
    memoization: bool,
    reduce_tree: bool,
    skipws: bool,
    ws: str,
) -> None:
    ParserPython(
        empty,
        comment_def,
        syntax_classes,
        autokwd=autokwd,
        debug=debug,
        ignore_case=ignore_case,
        memoization=memoization,
        reduce_tree=reduce_tree,
        skipws=skipws,
        ws=ws,
    )
