#!/usr/bin/python3
"""
BaseModel Module: Parent class for data model instances
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class handles the initialization,
    serialization, and deserialization of instances
    """

    def __init__(self, *args, **kwargs):
        """Initialize a BaseModel instance"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)

    def __str__(self):
        """String representation of a BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__)

    def __repr__(self):
        """Return string representation of BaseModel class"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__)

    def save(self):
        """Update 'updated_at' instance with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel class."""
        nw_dict = dict(self.__dict__)
        nw_dict['__class__'] = self.__class__.__name__
        nw_dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        nw_dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")

        return nw_dict

