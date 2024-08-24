#functions that collectively test the implementation of shorten thoroughly

from twttr import shorten

def test_string():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("PYTHON") == "PYTHN"
    assert shorten("hello, world") == "hll, wrld"


def test_other():
    assert shorten("CS50") == "CS50"
    assert shorten("@#$%") == "@#$%"


def test_empty():
    assert shorten("") == ""
