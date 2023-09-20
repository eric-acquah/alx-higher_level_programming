#!/usr/bin/python3

"""
Defining a new class that inherits from Rectangle.
`Square`

"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class inherits all attributes of Rectangtle
    But adds a few modifications to it to suit the
    properties of a square `a  rectangle with equle sides`
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize Square instance

        Args:
            size (int): the value of the sides of a square
            x (int): x value for the square calss
            y (int): y value for the square calss
            id (int): id value for the square calss
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """definig getter/setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Change the instance atrributes

        Args:
            args (tuple): list of arguments
            kwargs (dict): dictionary of new argumnts
        """
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
                # Check instance where fewer arguments are given
            except IndexError:
                return
        else:
            for key in kwargs:
                if key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]
                elif key == "id":
                    self.id = kwargs[key]
                else:
                    return

    def to_dictionary(self):
        """return a dictionary representation of the Square class"""
        self.Class_dict = {"size": self.size, "x": self.x,
                           "y": self.y, "id": self.id}
        return self.Class_dict
