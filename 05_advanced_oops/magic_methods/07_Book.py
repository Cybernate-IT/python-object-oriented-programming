class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # String representation using __str__
        return f"{self.title} by {self.author}"

    def __len__(self):
        # Length representation using __len__
        return self.pages

    def __eq__(self, other):
        # Equality comparison using __eq__
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        else:
            return False

# Creating instances of Book
book1 = Book("Python Basics", "John Doe", 200)
book2 = Book("Advanced Python", "Jane Smith", 300)
book3 = Book("Python Basics", "John Doe", 200)

# Using magic methods
print("String Representation:", book1)
print("Length of Book1:", len(book1))
print("Equality Comparison (book1 == book2):", book1 == book2)
print("Equality Comparison (book1 == book3):", book1 == book3)
