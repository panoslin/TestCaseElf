#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/1/7
# IDE: PyCharm
from test_case_elf.pipe import (
    to_csv,
    to_df,
    to_json
)
# typing
from typing import (
    Iterable,
    Optional,
    Union,
    TypeVar
)

SelfField = TypeVar("SelfField", bound="Field")


class Field:
    """
    Defining __add__ and __mul__ methods
    so that it can chain with other objects like:

        List[Dict] + field_instance
        List[Dict] * field_instance

    Defining __radd__ and __rmul__ methods
    so that it can chain with other objects like (in reverse order):

        field_instance + List[Dict]
        field_instance * List[Dict]

    """

    def __init__(self, **kwargs):
        self.field: Optional[dict] = kwargs

    def __add__(self, other: Union[Iterable, SelfField]):
        """
        field + Union[field, Iterable] (__add__)
        """
        if isinstance(other, Iterable):
            result = []
            for ele in other:
                result.append({**self.field, **ele})
            return result
        else:
            return {**self.field, **other.field}

    def __radd__(self, other: Iterable):
        """
        Iterable + field (__radd__)

        These functions are only called if the left operand does not support the corresponding operation
        and the operands are of different types.
        """
        return [{**ele, **self.field} for ele in other]

    def __mul__(self, other):
        """
        field * field (__mul__) -> self * other
        """
        left, right = self.field, other.field
        result = []
        field_key = next(iter(right))
        for field_value in right[field_key]:
            result.append({**left, **{field_key: field_value}})
        return result

    def __rmul__(self, other):
        """
        Iterable * field (__rmul__) -> Iterable * self

        These functions are only called if the left operand does not support the corresponding operation
        and the operands are of different types.
        """
        result = []
        field_key = next(iter(self.field))
        for ele in other:
            for field_value in self.field[field_key]:
                result.append({**ele, **{field_key: field_value}})
        return result


if __name__ == '__main__':
    from pprint import pprint

    pprint(
        (
                Field(region='Earthman')
                * Field(lastname=['Jackson', 'Gadot'])
                * Field(firstname=['Michael', 'Gal'])
                + Field(age=10)
                | to_json
        ),
    )
