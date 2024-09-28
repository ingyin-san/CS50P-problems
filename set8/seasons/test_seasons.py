#functions that test the implementation of convert function in seasons.py

import pytest
from seasons import convert
from datetime import date


def test_invalid_format():
    with pytest.raises(ValueError):
        convert(date.today(), "January 1, 2020")
        convert(date.today(), "2015/3/25")
        convert(date.today(), "12/12/2010")

def test_valid_format():
    with pytest.raises(ValueError):
        convert(date.today(), "30-09-2012")
        convert(date.today(), "07-25-2018")

    assert convert(date(2024, 9, 24), "2023-09-25") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(date(2024, 9, 25), "2023-09-25") == "Five hundred twenty-seven thousand forty minutes"
    assert convert(date(2024, 9, 24), "2022-09-25") == "One million, fifty-one thousand, two hundred minutes"
    assert convert(date(2024, 9, 25), "2022-09-25") == "One million, fifty-two thousand, six hundred forty minutes"
