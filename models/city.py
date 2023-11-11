#!/usr/bin/python3
"""Define city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class

    Attributes:
        state_id (str): state id
        name (str): city name
    """
    state_id = ""
    name = ""
