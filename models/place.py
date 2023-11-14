#!/usr/bin/python3
"""Define place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class

    Attributes:
        city_id (str): id of city
        user_id (str): id of user
        name (str): city name
        description (str): city description
        number_rooms (int): room count
        number_bathrooms (int): bathroom count
        max_guest (int): max guest count
        price_by_night (int): price by night
        latitude (float): place latitude
        longitude (float): place longitude
        amenity (list): amenity list
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity = []
