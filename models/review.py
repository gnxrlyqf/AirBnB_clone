#!/usr/bin/python3
"""Define review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class

    Attributes:
        place_id (str): place id
        user_id (str): user_id
        text (str): review content
    """
    place_id = ''
    user_id = ''
    text = ''
