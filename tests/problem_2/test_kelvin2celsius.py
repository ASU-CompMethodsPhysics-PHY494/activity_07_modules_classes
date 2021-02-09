# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem2.py'
POINTS = 2

def test_kelvin2celsius():
    return _test_variable("t_boil", 100.0,
                          FILENAME,
                          check_type=False)
