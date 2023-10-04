from __future__ import annotations

from collections.abc import Collection, Generator
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

_T = TypeVar("_T")


@dataclass
class DefaultAndValues(Generic[_T]):
    default: _T
    values: Collection[_T]


def iter_pos_args(
    *args: DefaultAndValues[Any],
) -> Generator[tuple[Any, ...], None, None]:
    defaults = tuple(arg.default for arg in args)

    yield (), *defaults

    for i, arg in enumerate(args):
        j = i + 1
        for value in arg.values:
            yield (*defaults[:i], value), *defaults[:i], value, *defaults[j:]


def iter_kw_args(
    **kwargs: DefaultAndValues[Any],
) -> Generator[tuple[Any, ...], None, None]:
    yield {}, *(arg.default for arg in kwargs.values())
    for name, arg in kwargs.items():
        for value in arg.values:
            yield {name: value}, *(
                value if name_ == name else arg_.default
                for name_, arg_ in kwargs.items()
            )
