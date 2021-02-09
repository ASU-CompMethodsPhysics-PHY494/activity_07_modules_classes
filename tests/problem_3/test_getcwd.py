import pathlib
import os

from ..tst import get_attribute

def test_getcwd():
    current_dir = pathlib.Path(os.curdir).absolute()
    value = get_attribute("cwd", "problem3.py")
    assert current_dir.samefile(value), f"cwd = '{value}' does not equal '{current_dir}'"
