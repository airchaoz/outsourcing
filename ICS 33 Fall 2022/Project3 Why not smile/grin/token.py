# token.py
#
# ICS 33 Fall 2022
# Project 3: Why Not Smile?
#
# Classes used to describe tokens in a Grin program.
#
# * GrinToken, which describes one token in its entirety.
# * GrinTokenKind, which identifies a type of token, such as a literal integer
#   or the keyword SUB.
# * GrinTokenCategory, which kinds of tokens into broader categories.
#
# WHAT YOU'LL NEED TO DO: Nothing.  This module is provided in its entirety,
# and it should not be necessary to change it.

from dataclasses import dataclass
from enum import Enum
from grin.location import GrinLocation
from typing import Any



class GrinTokenCategory(Enum):
    """A categorization of Grin tokens, which combines multiple kinds of
    Grin tokens together when they serve similar purposes."""
    COMPARISON_OPERATOR = 1
    IDENTIFIER = 2
    KEYWORD = 3
    LITERAL_VALUE = 4
    PUNCTUATION = 5



class GrinTokenKind(Enum):
    """Identifies a kind of Grin token."""
    ADD = (1, GrinTokenCategory.KEYWORD)
    COLON = (2, GrinTokenCategory.PUNCTUATION)
    DIV = (3, GrinTokenCategory.KEYWORD)
    DOT = (4, GrinTokenCategory.PUNCTUATION)
    END = (5, GrinTokenCategory.KEYWORD)
    EQUAL = (6, GrinTokenCategory.COMPARISON_OPERATOR)
    GOSUB = (7, GrinTokenCategory.KEYWORD)
    GOTO = (8, GrinTokenCategory.KEYWORD)
    GREATER_THAN = (9, GrinTokenCategory.COMPARISON_OPERATOR)
    GREATER_THAN_OR_EQUAL = (10, GrinTokenCategory.COMPARISON_OPERATOR)
    IDENTIFIER = (11, GrinTokenCategory.IDENTIFIER)
    IF = (12, GrinTokenCategory.KEYWORD)
    INNUM = (13, GrinTokenCategory.KEYWORD)
    INSTR = (14, GrinTokenCategory.KEYWORD)
    LESS_THAN = (15, GrinTokenCategory.COMPARISON_OPERATOR)
    LESS_THAN_OR_EQUAL = (16, GrinTokenCategory.COMPARISON_OPERATOR)
    LET = (17, GrinTokenCategory.KEYWORD)
    LITERAL_FLOAT = (18, GrinTokenCategory.LITERAL_VALUE)
    LITERAL_INTEGER = (19, GrinTokenCategory.LITERAL_VALUE)
    LITERAL_STRING = (20, GrinTokenCategory.LITERAL_VALUE)
    MULT = (21, GrinTokenCategory.KEYWORD)
    NOT_EQUAL = (21, GrinTokenCategory.COMPARISON_OPERATOR)
    PRINT = (22, GrinTokenCategory.KEYWORD)
    RETURN = (23, GrinTokenCategory.KEYWORD)
    SUB = (24, GrinTokenCategory.KEYWORD)


    _index: int
    _category: GrinTokenCategory


    def __init__(self, index: int, category: GrinTokenCategory):
        self._index = index
        self._category = category


    @property
    def index(self) -> int:
        """An index associated with this kind of token, mainly to differentiate
        it from all the others."""
        return self._index


    @property
    def category(self) -> GrinTokenCategory:
        """How this kind of token is categorized."""
        return self._category



@dataclass(frozen = True, kw_only = True)
class GrinToken:
    """A single token in a Grin program"""
    kind: GrinTokenKind
    text: str
    location: GrinLocation
    value: Any = None



__all__ = [
    GrinToken.__name__,
    GrinTokenCategory.__name__,
    GrinTokenKind.__name__
]
