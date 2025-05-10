# aggregation represents the relationship between one object and more (INDEPENDENT)object
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):  # book is a parameter
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Creating library instance
library = Library('Indian Library for Abroad')

# Creating book instances
book1 = Book('It Need With You', 'Rakesh Sharma')
book2 = Book('Time Slips Away', 'Mohan')

# Adding books to the library
library.add_book(book1)
library.add_book(book2)

# Output
print(library.name)
print("Books in the library:")
for book in library.list_books():
    print(book)
