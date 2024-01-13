#!/usr/bin/python3
"""
Define class FileStorage Module
"""
import json
import models


class FileStorage:
    """
    Serializes instances to JSON file and deserializes to JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary
        """
        return self.__objects

    def new(self, obj):
        """
        Set new obj into __objects
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        value_dict = obj.to_dict()
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serializes the objects into JSON file
        """
        objects_dict = {key: val for key, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd, default=lambda o: o.__dict__)

    def reload(self):
        """
        Reload the file and deserializes JSON into __objects
        """
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")

