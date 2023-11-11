#!/usr/bin/python3
"Define base model class"
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """BaseModel object constructor

        Args:
            *args (any): unused
            **kwargs (dict): keyword arguments
        """
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()
        if len(kwargs) == 0:
            models.storage.new(self)
        else:
            for key in kwargs:
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

    def __str__(self):
        """Class string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Save objects to storage"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Dictionary representation of class"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = str(self.__class__.__name__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
