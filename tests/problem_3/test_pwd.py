# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 3

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'problem3.py'
POINTS = 1

def test_python3():
    assert_python3()

def test_pwd():
    return _test_output(FILENAME,
                        r"""cwd = '/.*/activity.*'""",
                        input_values=None,
                        regex=True)


