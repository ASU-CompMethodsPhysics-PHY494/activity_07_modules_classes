# -*- coding: utf-8 -*-
# ASSIGNMENT: Activity 07 (Modules and Classes)
# PROBLEM NUMBER: 3

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'problem3.py'
POINTS = 4

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[95, 88.6, 6.3], [79.6, 88.6, 6.3], [1.0], [1.0, 0.0, 1.0], [2.0, 0.0, 1.0], [-10, -10, 2.5]], [{}, {}, {}, {}, {}, {}], [0.8451550699150085, 0.07656372550983487, 0.841344746068543, 0.841344746068543, 0.9772498680518207, 0.5])))
def test_Gaussian_CDF_with_erf(args, kwargs, reference):
    return _test_function("Phi",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False)
