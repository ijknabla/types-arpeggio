from __future__ import annotations

from collections.abc import Collection, Generator
from typing import TYPE_CHECKING, Any

import pytest
from arpeggio import EOF, ParserPython

if TYPE_CHECKING:
    from arpeggio import _ParsingExpressionLike


def optional_keyword_generator(
    *args: Collection[Any],
) -> Generator[tuple[Any | None, ...], None, None]:
    ndim = len(args)
    yield (None,) * ndim
    for i, collection in enumerate(args):
        for item in collection:
            yield tuple(item if j == i else None for j, _ in enumerate(args))


@pytest.mark.parametrize(
    """
    autokwd,
    debug,
    ignore_case,
    memoization,
    reduce_tree,
    skipws,
    ws,
    """,
    optional_keyword_generator(
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
        autokwd=autokwd,
        debug=debug,
        ignore_case=ignore_case,
        # memoization=memoization,  # TODO: match arpeggio version
        reduce_tree=reduce_tree,
        skipws=skipws,
        ws=ws,
    )


def empty() -> _ParsingExpressionLike:
    return EOF
