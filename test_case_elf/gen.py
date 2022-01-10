#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by panos on 2022/1/10
# IDE: PyCharm

import json
import pandas as pd
# typing
from typing import (
    List,
    Dict,
    TypeVar,
)

SelfField = TypeVar("SelfField", bound="TestCase")


class TestCase:
    def __init__(self):
        self.fix_fields = dict()
        self.var_fields = dict()
        self.series = []
        self.funcs = dict()

    def add_fix(self, **kwargs):
        self.fix_fields.update(kwargs)
        return self

    def add_var(self, **kwargs):
        self.var_fields.update(kwargs)
        return self

    def add_serie(self, name, start=0, step=1):
        self.series.append((name, start, step))
        return self

    def add_func(self, **kwargs):
        self.funcs.update(kwargs)
        return self

    def __construct_kv(self) -> List[Dict]:
        """
        # 1. construct fix field
        # 2. construct var field
        # 3. construct series
        # 4. apply function and append to new field
        :return:
        """

        # 1. construct fix field
        result = [self.fix_fields]

        # 2. construct var field
        for key, choices in self.var_fields.items():
            multiplier = []
            for base in result:
                for value in choices:
                    multiplier.append({**base, **{key: value}})
            result = multiplier

        # 3. construct series
        for name, start, step in self.series:
            i = start
            for test_case in result:
                test_case.update({name: i})
                i += step

        # 4. apply function and append to new field
        for key, func in self.funcs.items():
            for test_case in result:
                test_case.update({key: func(test_case)})

        return result

    def to_df(self, **kwargs):
        return pd.DataFrame(self.to_dict(), **kwargs)

    def to_csv(self, path, **kwargs):
        return pd.DataFrame(self.to_dict()).to_csv(path, index=False, **kwargs)

    def to_json(self, **kwargs):
        return json.dumps(self.to_dict(), **kwargs)

    def to_dict(self):
        return self.__construct_kv()


if __name__ == '__main__':
    from pprint import pprint
    import time
    pprint(
        (
            TestCase()
                .add_fix(
                region='Earthman',
                age=10
            )
                .add_var(
                firstname=['Gal', 'Michael'],
                lastname=['Gadot', 'Jackson']
            )
                .add_serie(name='id', start=1, step=1)
                .add_serie(name='id_desc', start=4, step=-1)
                .add_func(timestamp=lambda x: int(time.time()))
                .to_df()
        )
    )
