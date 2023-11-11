#!/usr/bin/python3
"""Define user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class

    Attributes:
        email (str): user email
        password (str): user password
        firs_name (str): user first name
        last_name (str): user last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
