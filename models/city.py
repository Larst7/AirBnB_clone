#!/usr/bin/python3
"""
City Module: Defines the City class
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherits from BaseModel
    """
    # Public class attributes initialized to empty strings
    state_id = ""
    name = ""
