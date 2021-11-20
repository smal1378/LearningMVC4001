# controller.py - connector of model and view
import model
import view


core_obj = model.Core()


def function1_add_book(name, author):
    core_obj.add_book(name, author)


win = view.UserPanel(core_obj.get_books(), function1_add_book)
win.mainloop()

