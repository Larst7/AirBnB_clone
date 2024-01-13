#!/usr/bin/python3
"""
Tests for the State model.
"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test the State class.
    """

    def test_state_inheritance(self):
        """
        Test that State class inherits from BaseModel.
        """
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_state_attributes(self):
        """
        Test that State class contains the attribute `name`.
        """
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_state_attribute_type(self):
        """
        Test that State class attribute name is of type str.
        """
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)


if __name__ == "__main__":
    unittest.main()

