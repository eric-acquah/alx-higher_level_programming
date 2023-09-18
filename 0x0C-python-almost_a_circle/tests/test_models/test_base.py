"""
Testing the base class
"""

import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """Run test for base class"""

    def test_instance1(self):
        make = Base(12)
        self.assertEqual(make.id, 12)

    def test_instance2(self):
        unmake = Base()
        self.assertEqual(unmake.id, 1)


if __name__ == "__main__":
    unittest.main()
