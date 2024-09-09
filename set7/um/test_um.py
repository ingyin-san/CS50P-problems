#functions that collectively test your implementation of count thoroughly

from um import count

def test_none():
    assert count(" ") == 0
    assert count("hello, world") == 0
    assert count("yummy") == 0

def test_count():
    assert count("um, um, um") == 3
    assert count("um, hello, um...") == 2
    assert count(" um.... hey....") == 1

def test_capital():
    assert count("Um, hi") == 1
    assert count("Um, Um...") == 2
