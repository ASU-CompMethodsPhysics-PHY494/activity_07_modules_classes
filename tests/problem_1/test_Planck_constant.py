# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'constants.py'
POINTS = 2

def test_Planck_constant():
    return _test_variable("h", 6.62607015e-34,
                          FILENAME,
                          check_type=False)
