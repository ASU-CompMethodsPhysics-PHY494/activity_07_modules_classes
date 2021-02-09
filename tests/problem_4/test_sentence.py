# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 4

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'problem4.py'
POINTS = 1

def test_sentence():
    return _test_variable("sentence", "MAY THE FORCE BE WITH YOU!",
                          FILENAME,
                          check_type=False)
