"""
This modules define the Rectangle `class`
Inherits from `Base`

"""
from models.base import Base

class Rectangle(Base):
    """Defines `Rectangle`"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize instances

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x: x coordinate of rectangle
            y: y coordinate of rectangle
        """
        # Handeling exceptions:
        self.__width = width
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        elif self.__width <= 0:
            raise ValueError("width must be > 0")

        self.__height = height
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        elif self.__height <= 0:
            raise ValueError("height must be > 0")

        self.__x = x
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        elif self.__x < 0:
            raise ValueError("x must be >= 0")

        self.__y = y
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        elif self.__y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        if not isinstance(self.id, int):
            raise TypeError("id must be an integer")


    # Define getters and setters for each private instance attribute

    @property
    def width(self):
        """ getter for `width` """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for `height` """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter for `x` """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter for `y` """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
