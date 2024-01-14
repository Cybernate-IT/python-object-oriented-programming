# Example of a Class with Attributes and Methods

# Class definition
class Book:
    def __init__(self, title, author, pages):
        # Attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.is_open = False

    # Method to display book information
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Status: {'Open' if self.is_open else 'Closed'}")

    # Method to open the book
    def open_book(self):
        if not self.is_open:
            print(f"{self.title} is now open.")
            self.is_open = True
        else:
            print(f"{self.title} is already open.")

    # Method to read a specific number of pages
    def read_pages(self, num_pages):
        if self.is_open:
            print(f"Reading {num_pages} pages of {self.title}.")
        else:
            print(f"{self.title} is closed. Open it first to start reading.")

# Creating instances of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 320)

# Displaying information about the books
print("Book 1 Information:")
book1.display_info()

print("\nBook 2 Information:")
book2.display_info()

# Opening and reading pages of the books
book1.open_book()
book1.read_pages(20)

book2.open_book()
book2.read_pages(50)
