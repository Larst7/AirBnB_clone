#!/usr/bin/python3
"""Test for the console"""

import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Class for testing the console"""

    def create(self):
        """Create the instance of HBNBCommand"""
        return HBNBCommand()

    def test_quit(self):
        """Test for the quit command"""
        con = self.create()
        result = con.onecmd("quit")
        self.assertIsNone(result)

    def test_EOF_handling(self):
        """Test for handling EOF"""
        con = self.create()
        result = con.onecmd("EOF")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()

