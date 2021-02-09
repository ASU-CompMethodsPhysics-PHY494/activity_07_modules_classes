# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_output, assert_python3

FILENAME = 'problem1.py'
POINTS = 1

def test_python3():
    assert_python3()

def test_print_hbar():
    return _test_output(FILENAME,
                        r"""hbar\s*=\s*1\.054571818e-34""",
                        input_values=None,
                        regex=True)


