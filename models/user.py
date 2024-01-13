#!/usr/bin/python3
"""
User Module: Defines the User class
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    # Public class attributes initialized to empty strings
    email = ""
    password = ""
    first_name = ""
    last_name = ""

