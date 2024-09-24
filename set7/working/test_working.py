#functions that collectively test your implementation of convert thoroughly

import pytest
from working import convert

def test_separator():
    with pytest.raises(ValueError):
        convert("2 AM - 6 PM")
        convert("8:00 AM - 12:00 PM")

def test_hour():
    with pytest.raises(ValueError):
        convert("0:30 AM to 2:00 AM")
        convert("12:00 PM to 13:00 PM")

    assert convert("9:00 AM to 3:00 PM") == "09:00 to 15:00"

def test_minute():
    with pytest.raises(ValueError):
        convert("10:60 AM to 12:00 AM")
        convert("3:00 PM to 4:99 PM")

    assert convert("6:30 PM to 8:59 PM") == "18:30 to 20:59"
