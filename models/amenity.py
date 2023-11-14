#!/usr/bin/python3
"""Define amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class

    Attributes:
        name (str): amenity name
    """
    name = ''
