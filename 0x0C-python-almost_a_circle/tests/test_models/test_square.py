#!/usr/bin/python3

"""
Testing of the Sqaure class

"""

from unittest.mock import patch
import unittest
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):
    """Testing is of square is done here"""

    def test_instantiation(self):
        """Testing instantiation"""
        new = Square(2, 7, 9, 16)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 7)
        self.assertEqual(new.y, 9)
        self.assertEqual(new.id, 16)

    def test_methods(self):
        """Testing methods"""
        new = Square(2, 2)
        self.assertEqual(new.area(), 4)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print(new)

            output = mock_stdout.getvalue()

            self.assertEqual(output, "[Square] (1) 2/0 - 2\n")

    def test_exceptions(self):
        """Testing how square handels exceptions"""

        with self.assertRaises(TypeError):
            new = Square("10", 2)

        with self.assertRaises(ValueError):
            new = Square(0, 2)
