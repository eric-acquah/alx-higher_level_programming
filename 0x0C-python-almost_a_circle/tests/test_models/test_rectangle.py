"""
Test rectangle class
"""


import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Test all scenarios"""

    def test_instanceId(self):
        new_id = Rectangle(10, 2)
        self.assertEqual(new_id.id, 4)

        another_id = Rectangle(2, 10)
        self.assertEqual(another_id.id, 5)

        id_again = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(id_again.id, 12)

    def test_instanceAttribute(self):
        new = Rectangle(10, 2)
        self.assertEqual(new.id, 3)
        self.assertEqual(new.width, 10)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)

    def test_instanceAttributeTypeException(self):
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
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 0, 0, 12)

        with self.assertRaises(ValueError):
            Rectangle(10, 0, 0, 0, 12)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, -10, 0, 12)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -7, 12)

    def test_instance_getters_setters(self):
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
        r1 = Rectangle(10, 2, 4, 6)

        with self.assertRaises(ValueError):
            r1.width = 0

        with self.assertRaises(ValueError):
            r1.height = 0

        with self.assertRaises(ValueError):
            r1.x = -11

        with self.assertRaises(ValueError):
            r1.y = -12
