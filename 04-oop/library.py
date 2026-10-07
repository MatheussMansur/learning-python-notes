# library example from the module, with check out added


class LibraryBook:
    def __init__(self, title, author, year, call_number):
        self.title = title
        self.author = author  # (last name, first name)
        self.year = year
        self.call_number = call_number
        self.checked_out = False

    def title_and_author(self):
        return "{} {}: {}".format(self.author[1], self.author[0], self.title)

    def check_out(self):
        if self.checked_out:
            return False
        self.checked_out = True
        return True

    def give_back(self):
        self.checked_out = False

    def __str__(self):
        return "{} {} ({}): {}".format(self.author[1], self.author[0], self.year, self.title)

    def __repr__(self):
        return "<Book: {} ({})>".format(self.title, self.call_number)


class EBook(LibraryBook):
    # ebooks never run out, so check out always works
    def check_out(self):
        return True


book = LibraryBook("Dom Casmurro", ("Assis", "Machado de"), 1899, "B869.3 A848d")
ebook = EBook("O Cortico", ("Azevedo", "Aluisio"), 1890, "B869.3 A994c")

print(book)
print(repr(book))
print(book.title_and_author())

print("first check out:", book.check_out())
print("second check out:", book.check_out())
book.give_back()
print("after giving back:", book.check_out())

print("ebook:", ebook.check_out(), ebook.check_out())
print(isinstance(ebook, LibraryBook))
