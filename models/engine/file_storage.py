#!/usr/bin/python3
"""Class FileStorage that serializes instances to a
JSON file and deserializes JSON file to instances
"""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(temp, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                from models.base_model import BaseModel
                data = json.load(f)
                for k, v in data.items():
                    # self.__objects[k] = BaseModel(**v)
                    self.__objects[k] = eval("{}(**v)".format(k.split(".")[0]))
        except:
            pass
