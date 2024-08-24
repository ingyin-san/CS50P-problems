#functions that collectively test the implementations of convert and gauge thoroughly

import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("1/3") == 33
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(90) == "90%"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("100/0")


def test_value():
    with pytest.raises(ValueError):
        convert("two/four")
        convert("5/4")
        convert("2.5/3")

