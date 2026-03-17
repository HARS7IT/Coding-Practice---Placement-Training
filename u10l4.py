# ------------------ BOOK CLASS ------------------
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}")


# ------------------ LIBRARY CLASS ------------------
class Library:
    def __init__(self):
        self.books = []   # List to store books

    # Add a book
    def add_book(self, book):
        book=input("Enter the name of the book: ")
        self.books.append(book)
        print("Book added successfully.")

    # Search book by title
    def search_by_title(self, title):
        title=input('Enter the title: ')
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("\nBooks in Library:")
            for book in self.books:
                book.display()



library = Library()

# Adding books
library.add_book(Book(101, "Python Basics", "Guido"))
library.add_book(Book(102, "Data Structures", "Mark Weiss"))
library.add_book(Book(103, "Operating Systems", "Silberschatz"))

# Display all books
library.display_books()

# Search a book
title = "Data Structures"
book = library.search_by_title(title)

if book:
    print("\nBook Found:")
    book.display()
else:
    print("\nBook not found.")



