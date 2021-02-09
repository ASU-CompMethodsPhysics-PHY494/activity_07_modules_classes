# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 5

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'ball.py'
POINTS = 2

def test_ball_volume():
    return _test_variable("volume", 33.510321638291124,
                          FILENAME,
                          check_type=False)
