# location.py
#
# ICS 33 Fall 2022
# Project 3: Why Not Smile?
#
# Defines a class called GrinLocation, whose objects describe a location within
# the text of a Grin program (i.e., a line number and a column number).
#
# WHAT YOU'LL NEED TO DO: Nothing.  This module is provided in its entirety,
# and it should not be necessary to change it.

from dataclasses import dataclass


@dataclass(frozen = True)
class GrinLocation:
    """Describes a location within the text of a Grin program"""


    line: int
    column: int


    def __post_init__(self):
        if int(self.line) < 1:
            raise ValueError(f'Line in location cannot be non-positive, was {self.line}')

        if int(self.column) < 1:
            raise ValueError(f'Column in location cannot be non-positive, was {self.column}')


    def __str__(self) -> str:
        return f'Line {self.line} Column {self.column}'



__all__ = [GrinLocation.__name__]
