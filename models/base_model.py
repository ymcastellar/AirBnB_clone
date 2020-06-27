#!/usr/bin/python3
"""Base class module
   defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base Model class"""

    def __init__(self):
        """Initialization
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """__str__ module
        Returns:
            [str]: human readable representation of an instance
        """
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute
           updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict module

        Returns:
            [dict]: dictionary representation of an instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
