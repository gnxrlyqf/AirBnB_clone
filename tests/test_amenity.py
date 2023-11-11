#!/usr/bin/python3
"""Unittest for amenity

Unittest classes:
    TestBaseModel_instance
    TestBaseModel_saving
    TestBaseModel_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instance(unittest.TestCase):
    """Unisttest for instantiating class"""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_args_kwargs(self):
        time = datetime.today()
        time_formatted = time.isoformat()
        amenity = Amenity("12", id="345", created_at=time_formatted, updated_at=time_formatted)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, time)
        self.assertEqual(amenity.updated_at, time)


class TestAmenity_saving(unittest.TestCase):
    """Unist test for saving class"""

    def test_save(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save(None)

    def test_save1(self):
        amenity = Amenity()
        sleep(0.05)
        update1 = amenity.updated_at
        amenity.save()
        self.assertLess(update1, amenity.updated_at)

    def test_update_file(self):
        amenity = Amenity()
        amenity.save()
        id = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(id, f.read())


class TestAmenity_dict(unittest.TestCase):
    """Unittest for to_dict"""

    def test_type(self):
        amenity = Amenity()
        self.assertTrue(dict, type(amenity.to_dict()))

    def test_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)

    def test_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_output(self):
        time = datetime.today()
        amenity = Amenity()
        amenity.id = "1234567890"
        amenity.created_at = amenity.updated_at = time
        dictionary = {
            'id': '1234567890',
            '__class__': 'Amenity',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(amenity.to_dict(), dictionary)

if __name__ == "__main__":
    unittest.main()