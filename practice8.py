class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("Book Found!")
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
                return
        print("Book not found")

    def display_books(self):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books:
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")

lib = Library()

while True:
    print("\n1. Add Book\n2. Search Book\n3. Display Books\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book id: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        book = Book(book_id, title, author)
        lib.add_book(book)

    elif choice == 2:
        title = input("Enter title to search: ")
        lib.search_book(title)

    elif choice == 3:
        lib.display_books()

    elif choice == 4:
        break

    else:
        print("Invalid choice")



