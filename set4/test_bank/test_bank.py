#functions that collectively test the implementation of value thoroughly

from bank import value

def test_hello():
    assert value("Hello") == 0
    assert value("  HELLO  ") == 0
    assert value("Hello, World") == 0


def test_h():
    assert value("Hey") == 20
    assert value("HI") == 20
    assert value("How you doing?") == 20

def test_other():
    assert value("What's happening?") == 100
    assert value("WHAT'S UP?") == 100

