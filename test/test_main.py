# tests/test_main.py
import sys
import os

# 親ディレクトリのsrcをPythonのパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import add, subtract, multiply

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 20) == -10
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0