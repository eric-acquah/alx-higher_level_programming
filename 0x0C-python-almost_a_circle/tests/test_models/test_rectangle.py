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
