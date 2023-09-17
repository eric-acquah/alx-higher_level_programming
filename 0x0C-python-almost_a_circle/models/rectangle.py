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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @property


    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        else:
            self.__y = value
