#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/1/9
# IDE: PyCharm
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/1/7
# IDE: PyCharm
import json
import pandas as pd
# typing
from pathlib import Path
from typing import (
    Union,
)


class Pipe(object):
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        return self.func(other)

    def __call__(self, *args, **kwargs):
        return Pipe(lambda x: self.func(x, *args, **kwargs))


@Pipe
def to_json(iterable):
    return json.dumps(iterable)


@Pipe
def to_df(iterable):
    return pd.DataFrame(iterable)


@Pipe
def to_csv(iterable, path: Union[str, Path], **kwargs):
    return pd.DataFrame(iterable).to_csv(path, index=False, **kwargs)

if __name__ == '__main__':
    from pprint import pprint
    pprint(
        (
            [
                {'a': 1, 'b': 2},
                {'c': 1, 'd': 2},
                {'e': 1, 'f': 2},
            ]
            | to_csv('test.csv')
        )
    )