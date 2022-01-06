#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/1/7
# IDE: PyCharm
from typing import List, Iterable, Union, Any

class VarField:
    def __init__(self):
        pass

class FixField:
    def __init__(self):
        pass
#
# class TestCase:
#     def __init__(self, *args, **kwargs):
#         print(locals())
#
#     def __str__(self, *args, **kwargs):
#         super(TestCase, self).__str__()
#
#     def chain_variable(self, name, variable: Iterable):
#         pass
#
#     def chain_constant(self, nema, constant: Any):
#         pass
#
#     def __repr__(self, *args, **kwargs):
#         super(TestCase, self).__repr__()
#
#
#     def __setitem__(self, *args, **kwargs):
#         """ Set self[key] to value. """
#         super(TestCase, self).__setitem__()

if __name__ == '__main__':
    a = TestCase(
        [1,2,3],
        [4,5,6],
        a=1
    )