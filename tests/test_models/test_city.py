#!/usr/bin/python3
"""Unittest for city

Unittest classes:
    TestBaseModel_instance
    TestBaseModel_saving
    TestBaseModel_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instance(unittest.TestCase):
    """Unisttest for instantiating class"""

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(City().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_args_kwargs(self):
        time = datetime.today()
        time_formatted = time.isoformat()
        city = City("12", id="345", created_at=time_formatted, updated_at=time_formatted)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, time)
        self.assertEqual(city.updated_at, time)

class TestCity_saving(unittest.TestCase):
    """Unist test for saving class"""

    def test_save(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_save1(self):
        city = City()
        sleep(0.05)
        update1 = city.updated_at
        city.save()
        self.assertLess(update1, city.updated_at)

    def test_update_file(self):
        city = City()
        city.save()
        id = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(id, f.read())


class TestCity_dict(unittest.TestCase):
    """Unittest for to_dict"""

    def test_type(self):
        city = City()
        self.assertTrue(dict, type(city.to_dict()))

    def test_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)

    def test_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_output(self):
        time = datetime.today()
        city = City()
        city.id = "1234567890"
        city.created_at = city.updated_at = time
        dictionary = {
            'id': '1234567890',
            '__class__': 'City',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(city.to_dict(), dictionary)

if __name__ == "__main__":
    unittest.main()