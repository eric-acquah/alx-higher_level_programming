"""
Test rectangle class
"""


import unittest
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
    """Test all scenarios"""

    def test_instanceId(self):
        new_id = Rectangle(10, 2)
        self.assertEqual(new_id.id, 1)

        another_id = Rectangle(2, 10)
        self.assertEqual(another_id.id, 2)

        id_again = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(id_again.id, 12)

    def test_instanceType(self):
        new = Rectangle(10, 2)
        self.assertEqual(new.id, 3)
        self.assertEqual(new.width, 10)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
