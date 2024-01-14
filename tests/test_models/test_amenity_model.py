#!/usr/bin/python3

"""
Test for the Amenity model.
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Testing Amenity class
    """

    def test_amenity_inheritance(self):
        """
        Test that the Amenity class Inherits from BaseModel
        """
        new_amenity = Amenity()
        self.assertIsInstance(new_amenity, BaseModel)

    def test_amenity_has_name_attribute(self):
        """
        Test that Amenity class has a name attribute.
        """
        new_amenity = Amenity()
        self.assertTrue(hasattr(new_amenity, "name"))

    def test_amenity_attribute_type(self):
        """
        Test that Amenity class has the correct type for the name attribute.
        """
        new_amenity = Amenity()
        name_value = getattr(new_amenity, "name")
        self.assertIsInstance(name_value, str)

if __name__ == "__main__":
    unittest.main()

