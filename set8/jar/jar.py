#a cookie jar in which cookies can be stored and removed

class Jar:
    def __init__(self, capacity=12):
        self.cookies = 0
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError


    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n <= self._capacity:
            self.cookies += n
        else:
            raise ValueError

    def withdraw(self, n):
        if self.cookies >= n:
            self.cookies -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
