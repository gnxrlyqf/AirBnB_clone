#!/usr/bin/python3
"""Unittest for place

Unittest classes:
    TestPlace_instance
    TestPlace_saving
    TestPlace_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instance(unittest.TestCase):
    """Unisttest for instantiating class"""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_args_kwargs(self):
        time = datetime.today()
        time_formatted = time.isoformat()
        place = Place("12", id="345", created_at=time_formatted,
                      updated_at=time_formatted)
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, time)
        self.assertEqual(place.updated_at, time)

    def test_place(self):
        place = Place()
        self.assertEqual(place.city_id, str)
        self.assertEqual(place.user_id, str)
        self.assertEqual(place.name, str)
        self.assertEqual(place.description, str)
        self.assertEqual(place.number_rooms, int)
        self.assertEqual(place.number_bathrooms, int)
        self.assertEqual(place.max_guest, int)
        self.assertEqual(place.price_by_night, float)
        self.assertEqual(place.latitude, float)
        self.assertEqual(place.longitude, float)
        self.assertEqual(place.amenity, list)


class TestPlace_saving(unittest.TestCase):
    """Unist test for saving class"""

    def test_save(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save1(self):
        place = Place()
        sleep(0.05)
        update1 = place.updated_at
        place.save()
        self.assertLess(update1, place.updated_at)

    def test_update_file(self):
        place = Place()
        place.save()
        id = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(id, f.read())


class TestPlace_dict(unittest.TestCase):
    """Unittest for to_dict"""

    def test_type(self):
        place = Place()
        self.assertTrue(dict, type(place.to_dict()))

    def test_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)

    def test_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_output(self):
        time = datetime.today()
        place = Place()
        place.id = "1234567890"
        place.created_at = place.updated_at = time
        dictionary = {
            'id': '1234567890',
            '__class__': 'Place',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(place.to_dict(), dictionary)


if __name__ == "__main__":
    unittest.main()
