# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 4

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem4.py'
POINTS = 2

def test_lower():
    return _test_variable("l_sentence", "may the force be with you!",
                          FILENAME,
                          check_type=False)
