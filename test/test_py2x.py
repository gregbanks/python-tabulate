# -*- coding: utf-8 -*-

"""Python 2.x tests."""

from tabulate import tabulate
from common import assert_equal


def test_format_with_mixed_values():
    expected = '\n'.join([
        '-----',
        '',
        'a',
        '0',
        'False',
        '-----',
    ])
    data = [[None], ['a'], [0], [False]]
    table = tabulate(data)
    assert_equal(table, expected)

