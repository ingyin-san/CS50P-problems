#functions that collectively test your implementation of is_valid thoroughly

from plates import is_valid

def test_start():
    assert is_valid("CS50") == True
    assert is_valid("C50S") == False
    assert is_valid("50") == False


def test_count():
    assert is_valid("CS") == True
    assert is_valid("PLATES") == True
    assert is_valid("C") == False
    assert is_valid("OUTOFTIME") == False


def test_num():
    assert is_valid("CTL879") == True
    assert is_valid("CS05") == False
    assert is_valid("AA22A") == False
    assert is_valid("CS50P2") == False


def test_other():
    assert is_valid("HI.34") == False
    assert is_valid(" LOL4 ") == False
    assert is_valid("HI,GUY") == False
    assert is_valid("CS:50") == False
    assert is_valid("HA!?") == False
