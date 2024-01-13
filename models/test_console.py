#!/usr/bin/python3
"""Test for the console"""

import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Class for testing the console"""

    def setUp(self):
        """Set up the console instance"""
        self.console = HBNBCommand()

    def test_quit(self):
        """Test the quit command"""
        result = self.console.onecmd("quit")
        self.assertTrue(result)

    def test_EOF(self):
        """Test the EOF command"""
        result = self.console.onecmd("EOF")
        self.assertFalse(result)  # Assuming EOF does not return True

if __name__ == "__main__":
    unittest.main()

