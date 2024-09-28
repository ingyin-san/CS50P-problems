#functions that collectively test the implementation of Jar

from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10

    with pytest.raises(ValueError):
        Jar(-3)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(7)

    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(5)


def test_withdraw():
    jar = Jar(13)

    jar.deposit(10)
    jar.withdraw(9)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.withdraw(2)
