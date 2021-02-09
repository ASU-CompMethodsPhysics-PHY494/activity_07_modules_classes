# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'problem2.py'
POINTS = 1

def test_python3():
    assert_python3()

def test_print_t_boil():
    return _test_output(FILENAME,
                        r"""Water boils at 100.00°C.""",
                        input_values=None,
                        regex=False)


