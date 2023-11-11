#!/usr/bin/python3
"""Define state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class

    Attributes:
        name (str): state name
    """
    name = ""
