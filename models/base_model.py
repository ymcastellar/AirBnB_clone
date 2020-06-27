#!/usr/bin/python3
"""Base class module
   defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """Base Model class"""

    def __init__(self, *args, **kwargs):
        """Initialization Base instance
        """
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if hasattr(self, "created_at")
                and type(self.created_at) == str:
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                if hasattr(self, "updated_at")
                and type(self.updated_at) == str:
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")

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
