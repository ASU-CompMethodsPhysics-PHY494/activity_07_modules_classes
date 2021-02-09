# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 3

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem3.py'
POINTS = 2

def test_sintau():
    return _test_variable("y_full_circle", 0.0,
                          FILENAME,
                          check_type=False)
