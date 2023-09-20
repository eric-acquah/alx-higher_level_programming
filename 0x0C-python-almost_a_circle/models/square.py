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

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
