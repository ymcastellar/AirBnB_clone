#!/usr/bin/python3
"""Class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
"""
import json
import datetime


class FileStorage:
    """FileStorage Class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(temp, f, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                from models.base_model import BaseModel
                data = json.load(f)
                for k, v in data.items():
                    self.__objects[k] = eval("{}(**v)".format(k.split(".")[0]))
        except Exception:
            pass

    def classes(self):
        """Return a dictionary of classes and references
        """
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    '''def attributes(self):
        """Return valid attributes and their types
        """
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime.datetime,
                 "updated_at": datetime.datetime}
        }
        return attributes'''
