from abc import ABC, abstractmethod

# Interface: Printable
class Printable(ABC):
    # Abstract method to be implemented by classes
    @abstractmethod
    def display(self):
        pass

# Class implementing the Printable interface
class Book(Printable):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Implementation of the display method from the Printable interface
    def display(self):
        print(f"Book: '{self.title}' by {self.author}")

# Class implementing the Printable interface
class Movie(Printable):
    def __init__(self, title, director):
        self.title = title
        self.director = director

    # Implementation of the display method from the Printable interface
    def display(self):
        print(f"Movie: '{self.title}' directed by {self.director}")

# Creating instances of classes that implement the Printable interface
book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
movie = Movie(title="Inception", director="Christopher Nolan")

# Displaying information using the display method from the Printable interface
book.display()
movie.display()
