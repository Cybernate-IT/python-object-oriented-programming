class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print("Width must be greater than 0.")

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print("Height must be greater than 0.")

    @width.deleter
    def width(self):
        print("Deleting width.")
        del self._width

    @height.deleter
    def height(self):
        print("Deleting height.")
        del self._height


# Creating an instance of the Rectangle class
rectangle = Rectangle(width=5, height=7)

# Accessing read-only properties
print("Width:", rectangle.width)
print("Height:", rectangle.height)
print("Area:", rectangle.area)
print("Perimeter:", rectangle.perimeter)

# Trying to modify read-only properties using setter methods
rectangle.width = 10
rectangle.height = 8

# Deleting properties using deleter methods
del rectangle.width
del rectangle.height
