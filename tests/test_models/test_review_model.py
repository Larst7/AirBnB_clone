#!/usr/bin/python3
"""
Test for the Review model.
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Testing Review class
    """

    def test_review_inheritance(self):
        """
        Test that the Review class Inherits from BaseModel
        """
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_review_attributes(self):
        """
        Test that Review class has place_id, user_id, and text
        attributes.
        """
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_review_attribute_types(self):
        """
        Test the types of place_id, user_id, and text attributes.
        """
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)


if __name__ == "__main__":
    unittest.main()

