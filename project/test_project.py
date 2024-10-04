#methods for testing the implementations of adding, editing, and deleting flashcards

from project import add, edit, delete
import csv

def test_add():
    add("5*6", "30")
    with open("flashcards.csv", 'r') as file:
        reader = csv.DictReader(file)
        cards = list(reader)
        assert {"question": "5*6", "answer": "30"} in cards


def test_edit():
    edit("5*6", "3*10")
    with open("flashcards.csv", 'r') as file:
        reader = csv.DictReader(file)
        cards = list(reader)
        assert {"question": "3*10", "answer": "30"} in cards


def test_delete():
    delete("30")
    with open("flashcards.csv", 'r') as file:
        reader = csv.DictReader(file)
        cards = list(reader)
        assert {"answer": "30"} not in cards
