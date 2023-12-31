#!/usr/bin/python3

"""
Test rectangle class
"""

from unittest.mock import patch
from io import StringIO
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Test all scenarios"""

    def test_instanceId(self):
        """check instance ids"""

        new_id = Rectangle(10, 2, 4, 7, 4)
        self.assertEqual(new_id.id, 4)

        id_again = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(id_again.id, 12)

    def test_instanceAttribute(self):
        """Check the other attributes"""

        new = Rectangle(10, 2)
        self.assertEqual(new.width, 10)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)

    def test_instanceAttributeTypeException(self):
        """Type exceptions with instance attributes"""

        with self.assertRaises(TypeError):
            Rectangle("10", 2, 0, 0, 12)

        with self.assertRaises(TypeError):
            Rectangle(10, "2", 0, 0, 12)

        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0", 0, 12)

        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0", 12)

        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, "12")

    def test_instanceAttributeValueException(self):
        """Exceptions at initailization level"""

        with self.assertRaises(ValueError):
            Rectangle(0, 2, 0, 0, 12)

        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0, 12)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, -10, 0, 12)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -7, 12)

    def test_instance_getters_setters(self):
        """check for instance getter/setter accuracy"""

        r1 = Rectangle(10, 2, 4, 6)
        r1.width += 1
        r1.height *= 2
        r1.x += 2
        r1.y += 2
        self.assertEqual(r1.width, 11)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 8)

    def test_getter_setter_TypeException(self):
        """ Check getter setter type exceptions """

        r1 = Rectangle(10, 2, 4, 6)

        with self.assertRaises(TypeError):
            r1.width += "1"

        with self.assertRaises(TypeError):
            r1.height += "1"

        with self.assertRaises(TypeError):
            r1.x += "1"

        with self.assertRaises(TypeError):
            r1.y += "1"

    def test_getter_setter_ValueException(self):
        """ Check getter setter value exceptions """

        r1 = Rectangle(10, 2, 4, 6)

        with self.assertRaises(ValueError):
            r1.width = 0

        with self.assertRaises(ValueError):
            r1.height = 0

        with self.assertRaises(ValueError):
            r1.x = -11

        with self.assertRaises(ValueError):
            r1.y = -12

    def test_area(self):
        """Test area method"""

        value = Rectangle(10, 2)
        self.assertEqual(value.area(), 20)

        value.width = 2
        value.height = 4
        self.assertEqual(value.area(), 8)

        value.width = 1
        value.height = 1
        self.assertEqual(value.area(), 1)

        with self.assertRaises(ValueError):
            value.width = -1

        with self.assertRaises(ValueError):
            value.height = 0

        with self.assertRaises(TypeError):
            value.width = "-1"

        with self.assertRaises(TypeError):
            value.height = "11"

    def test_display(self):
        """Test printed output"""

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            h1 = Rectangle(4, 2)

            h1.display()  # call display function

            output = mock_stdout.getvalue()  # capture stdout

            self.assertEqual(output, "####\n####\n")

    def test_display_XY(self):
        """Test printed output considering x and y values"""

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            h1 = Rectangle(4, 2, 1, 1)

            h1.display()  # call display function

            output = mock_stdout.getvalue()  # capture stdout

            self.assertEqual(output, "\n ####\n ####\n")

    def test_str(self):
        """Test overidden str method"""

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            ins = Rectangle(2, 4, 6, 8, 12)

            print(ins)  # make an implecit call to __str__ method

            output = mock_stdout.getvalue()

            self.assertEqual(output, "[Rectangle] (12) 6/8 - 2/4\n")

    def test_update(self):
        """Test the proper altering of the instance attributes"""

        new = Rectangle(3, 7, 9, 15, 21)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.id, 21)

        # test for changes
        new.update(2, 4, 6, 8, 10)
        self.assertEqual(new.width, 4)
        self.assertEqual(new.height, 6)
        self.assertEqual(new.x, 8)
        self.assertEqual(new.y, 10)
        self.assertEqual(new.id, 2)

        # edge cases
        new.update(4, 6, 8)
        self.assertEqual(new.width, 6)
        self.assertEqual(new.height, 8)
        self.assertEqual(new.x, 8)
        self.assertEqual(new.y, 10)
        self.assertEqual(new.id, 4)

    def test_updated_update(self):
        """Test the update to the update method"""
        new = Rectangle(3, 7, 9, 15, 21)
        self.assertEqual(new.width, 3)
        self.assertEqual(new.id, 21)

        # test for changes
        new.update(id=2, width=4, height=6, x=8, y=10)
        self.assertEqual(new.width, 4)
        self.assertEqual(new.height, 6)
        self.assertEqual(new.x, 8)
        self.assertEqual(new.y, 10)
        self.assertEqual(new.id, 2)

        # edge cases
        # kwargs must not work when args is present
        new.update(4, 6, 8, x=11, y=12)
        self.assertEqual(new.width, 6)
        self.assertEqual(new.height, 8)
        self.assertEqual(new.x, 8)
        self.assertEqual(new.y, 10)
        self.assertEqual(new.id, 4)

    def test_to_dict(self):
        """to_dicttionary test"""
        val = Rectangle(1, 2, 3, 4, 5)
        out_dict = {'width' : 1, 'height' : 2, 'x' : 3, 'y' : 4, 'id' : 5}
        self.assertEqual(val.to_dictionary(), out_dict)
