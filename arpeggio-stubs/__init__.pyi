from __future__ import annotations

import typing as _typing
from collections.abc import Callable as _Callable
from collections.abc import Iterable as _Iterable
from collections.abc import Sequence as _Sequence
from typing import IO as _IO
from typing import Any as _Any

from typing_extensions import Final as _Final
from typing_extensions import Literal as _Literal
from typing_extensions import NotRequired as _NotRequired
from typing_extensions import TypedDict as _TypedDict

_ParsingExpressionLike = (
    str
    | ParsingExpression
    | _Sequence[_ParsingExpressionLike]
    | _Callable[[], _ParsingExpressionLike]
)

DEFAULT_WS: _Final[_Literal["\t\n\r "]]

class NoMatch(Exception): ...

class DebugPrinter:
    debug: bool
    file: _IO[str]
    def __init__(
        self,
        *,
        # DebugPrinter
        debug: bool = ...,
        file: _IO[str] = ...,
    ) -> None: ...
    def dprint(
        self,
        message: str,
        indent_change: int = ...,
    ) -> None: ...

class ParsingExpression:
    rule_name: str
    root: bool
    nodes: _typing.MutableSequence[ParsingExpression]
    suppress: bool
    def __init__(
        self,
        # ParsingExpression
        *elements: _ParsingExpressionLike,
        rule_name: str = ...,
        root: bool = ...,
        nodes: _Iterable[ParsingExpression] = ...,
        suppress: bool = ...,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    def parse(self, parser: Parser) -> ParseTreeNode: ...

class Sequence(ParsingExpression):
    ws: str | None
    skipws: bool | None
    def __init__(
        self,
        # ParsingExpression
        *elements: _ParsingExpressionLike,
        rule_name: str = ...,
        root: bool = ...,
        nodes: _Iterable[ParsingExpression] = ...,
        suppress: bool = ...,
        # Sequence
        ws: str | None = ...,
        skipws: bool | None = ...,
    ) -> None: ...

class OrderedChoice(Sequence):
    def __init__(
        self,
        # ParsingExpression
        *elements: _ParsingExpressionLike,
        rule_name: str = ...,
        root: bool = ...,
        nodes: _Iterable[ParsingExpression] = ...,
        suppress: bool = ...,
        # Sequence
        ws: str | None = ...,
        skipws: bool | None = ...,
    ) -> None: ...

class Repetition(ParsingExpression):
    """
    eolterm: _typing.Any
    sep: _typing.Any
    """

    def __init__(
        self,
        *elements: _ParsingExpressionLike,
        rule_name: str = ...,
        root: bool = ...,
        nodes: _Iterable[_ParsingExpressionLike] = ...,
        suppress: bool = ...,
        sep: _ParsingExpressionLike = ...,
    ) -> None: ...
    sep: ParsingExpression | None

class Optional(Repetition): ...
class ZeroOrMore(Repetition): ...
class OneOrMore(Repetition): ...
class SyntaxPredicate(ParsingExpression): ...
class Not(SyntaxPredicate): ...
class Decorator(ParsingExpression): ...
class Combine(Decorator): ...

class Match(ParsingExpression):
    def __init__(
        self,
        rule_name: str,
        root: bool = ...,
    ) -> None: ...

class RegExMatch(Match):
    def __init__(
        self,
        to_match: str,
        rule_name: str = ...,
        root: bool = ...,
        ignore_case: bool = ...,
    ) -> None: ...
    def compile(self) -> None: ...

class StrMatch(Match):
    def __init__(
        self,
        to_match: str,
        rule_name: str = ...,
        root: bool = ...,
        ignore_case: bool = ...,
    ) -> None: ...

class EndOfFile(Match):
    def __init__(self) -> None: ...

def EOF() -> EndOfFile: ...

# __LINE__:966
class ParseTreeNode:
    rule: ParsingExpression
    rule_name: str
    position: int
    error: bool
    comments: _Any | None

    def __init__(
        self,
        rule: ParsingExpression,
        position: int,
        error: bool,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def position_end(self) -> int: ...
    def visit(self, visitor: PTNodeVisitor) -> _Any: ...
    def tree_str(self, indent: int = ...) -> str: ...

# __LINE__:1043
class Terminal(ParseTreeNode):
    value: str
    suppress: bool
    extra_info: _Any | None
    def __init__(
        self,
        rule: ParsingExpression,
        position: int,
        value: str,
        error: bool = ...,
        suppress: bool = ...,
        extra_info: _Any | None = ...,
    ) -> None: ...
    @property
    def desc(self) -> str: ...
    def flat_str(self) -> str: ...
    def __unicode__(self) -> str: ...

class NonTerminal(ParseTreeNode, list[ParseTreeNode]):
    def __init__(
        self,
        rule: ParsingExpression,
        nodes: _Iterable[ParseTreeNode],
        error: bool = ...,
        _filtered: bool = ...,
    ) -> None: ...
    @property
    def value(self) -> str: ...
    @property
    def desc(self) -> str: ...
    def flat_str(self) -> str: ...
    def __getattr__(self, rule_name: str) -> NonTerminal: ...

class PTNodeVisitor(DebugPrinter):
    def __init__(
        self,
        defaults: bool = ...,
        *,
        # DebugPrinter
        debug: bool = ...,
        file: _IO[str] = ...,
    ) -> None: ...

def visit_parse_tree(
    parse_tree: ParseTreeNode, visitor: PTNodeVisitor
) -> _typing.Any: ...

class Parser(DebugPrinter):
    skipws: bool
    ws: str
    reduce_tree: bool
    autokwd: bool
    ignore_case: bool
    memoization: bool
    parser_model: ParsingExpression
    comments_model: ParsingExpression | None
    def __init__(
        self,
        # Parser
        skipws: bool = ...,
        ws: str | None = ...,
        reduce_tree: bool = ...,
        autokwd: bool = ...,
        ignore_case: bool = ...,
        memoization: bool = ...,
        *,
        # DebugPrinter
        debug: bool = ...,
        file: _IO[str] = ...,
    ) -> None: ...
    def parse(
        self, _input: _typing.Any, file_name: _typing.Any = ...
    ) -> ParseTreeNode: ...

class CrossRef:
    target_rule_name: str
    def __init__(
        self,
        target_rule_name: str,
        position: int = ...,
    ) -> None: ...

class _SyntaxClasses(_TypedDict):
    StrMatch: _NotRequired[type[ParsingExpression]]
    OrderedChoice: _NotRequired[type[ParsingExpression]]
    Sequence: _NotRequired[type[ParsingExpression]]

class ParserPython(Parser):
    syntax_classes: _SyntaxClasses

    def __init__(
        self,
        # ParserPython
        language_def: _ParsingExpressionLike,
        comment_def: _ParsingExpressionLike | None = ...,
        syntax_classes: _SyntaxClasses | None = ...,
        # Parser
        skipws: bool = ...,
        ws: str | None = ...,
        reduce_tree: bool = ...,
        autokwd: bool = ...,
        ignore_case: bool = ...,
        memoization: bool = ...,
        *,
        # DebugPrinter
        debug: bool = ...,
        file: _IO[str] = ...,
    ) -> None: ...
    def _from_python(self, expression: _typing.Any) -> ParsingExpression: ...
