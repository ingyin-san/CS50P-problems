#functions that collectively test your implementation of validate thoroughly

from set7.numb3rs.numb3rs import validate

def test_string():
    assert validate("cat") == False
    assert validate(" Hello ") == False
    assert validate("What?") == False

def test_int():
    assert validate("0.0.0.0") == True
    assert validate("1.0.56.100") == True
    assert validate("85.92.74.53") == True
    assert validate("255.255.255.255") == True
    assert validate("275.3.6.28") == False
    assert validate("3.584.7.21") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("1.2") == False
    assert validate("5.6.7.8.9") == False
