from __future__ import annotations

from typing import TYPE_CHECKING

from arpeggio import ParsingExpression

if TYPE_CHECKING:
    from arpeggio import _ParsingExpressionLike


def _str() -> _ParsingExpressionLike:
    return ""


def _parsing_expression() -> _ParsingExpressionLike:
    return ParsingExpression()


def _callable() -> _ParsingExpressionLike:
    return _callable


def _sequence_1_a() -> _ParsingExpressionLike:
    return ("",)


def _sequence_1_b() -> _ParsingExpressionLike:
    return (ParsingExpression(),)


def _sequence_1_c() -> _ParsingExpressionLike:
    return (_callable,)


def _sequence_3() -> _ParsingExpressionLike:
    return (
        "",
        ParsingExpression(),
        _callable,
    )


def _sequence_1_0() -> _ParsingExpressionLike:
    return [[]]
