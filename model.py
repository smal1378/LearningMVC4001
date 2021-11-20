# Model.py
# by Esmail Mahjoor - t.me/smal1378
from typing import List


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __repr__(self):
        return self.name + " - " + self.author


class Core:
    def __init__(self):
        self.lst: List[Book] = list()  # or []

    def add_book(self, name, author):
        b = Book(name, author)
        self.lst.append(b)

    def get_books(self):
        return self.lst

