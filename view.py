# View.py - A module for GUI
# By Esmail
from tkinter import Tk, Button, Listbox, Toplevel, Label, Entry
from typing import Optional


class UserPanel(Tk):
    def __init__(self, lst, callback1):
        """
        Main User Panel
        :param lst: list of Books
        """
        super(UserPanel, self).__init__()
        self.callback1 = callback1
        self.title("Library Ver1.0")
        self.config(bg="white")
        Button(self, text="add book",
               command=self.add).grid(row=1, column=1, pady=5)
        self.lsbx = Listbox(self)
        self.lsbx.grid(row=2, column=1, pady=5, padx=5)
        for book in lst:
            self.lsbx.insert("end", book.name + " - " + book.author)

    def add(self):
        name = UserInput(self, "Get Name","Enter Book's Name:").get_res()
        author = UserInput(self, "Get Author","Enter Author's Name:").get_res()
        self.callback1(name, author)
        self.lsbx.insert("end", name + " - " + author)


class UserInput(Toplevel):
    def __init__(self, master, title: str, message: str):
        super(UserInput, self).__init__(master)
        self.res: Optional[str] = None
        self.title(title)
        Label(self, text=message).grid(row=1, column=1, padx=10, pady=10)
        self.ent = Entry(self, width=40)
        self.ent.grid(row=2, column=1, pady=5)
        Button(self, text="OK", command=self.ok).grid(row=3, column=1, pady=5)

    def ok(self):
        self.res = self.ent.get()
        self.destroy()

    def get_res(self) -> Optional[str]:
        self.res is None and self.wait_window()
        return self.res

