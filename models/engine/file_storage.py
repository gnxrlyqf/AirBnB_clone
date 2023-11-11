#!/usr/bin/python3
""""""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review


class FileStorage:
    """FileStorage class

    Attributes:
        file_path (str): file path
        objects (dict): all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Add new object to storage
        
        Args:
            obj (obj): object to add
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                dictionary = json.load(file)
                for value in dictionary.values():
                    name = value["__class__"]
                    del value["__class__"]
                    nclass = eval(name)
                    self.new(nclass(**value))
        except FileNotFoundError:
            return

    def save(self):
        dictionary = FileStorage.__objects
        new_dict = {}
        for e in dictionary:
            new_dict[e] = dictionary[e].to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_dict, file)
