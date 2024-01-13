#!/usr/bin/python3
"""
Review Module: Defines the Review class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherits from BaseModel
    """
    # Public class attributes initialized to empty strings
    place_id = ""
    user_id = ""
    text = ""

