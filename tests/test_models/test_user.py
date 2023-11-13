#!/usr/bin/python3
"""Unittest for user

Unittest classes:
    TestBaseModel_instance
    TestBaseModel_saving
    TestBaseModel_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instance(unittest.TestCase):
    """Unisttest for instantiating class"""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_args_kwargs(self):
        time = datetime.today()
        time_formatted = time.isoformat()
        user = User("12", id="345", created_at=time_formatted, updated_at=time_formatted)
        self.assertEqual(user.id, "345")
        self.assertEqual(user.created_at, time)
        self.assertEqual(user.updated_at, time)


class TestUser_saving(unittest.TestCase):
    """Unist test for saving class"""

    def test_save(self):
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)

    def test_save1(self):
        user = User()
        sleep(0.05)
        update1 = user.updated_at
        user.save()
        self.assertLess(update1, user.updated_at)

    def test_update_file(self):
        user = User()
        user.save()
        id = "User." + user.id
        with open("file.json", "r") as f:
            self.assertIn(id, f.read())


class TestUser_dict(unittest.TestCase):
    """Unittest for to_dict"""

    def test_type(self):
        user = User()
        self.assertTrue(dict, type(user.to_dict()))

    def test_arg(self):
        user = User()
        with self.assertRaises(TypeError):
            user.to_dict(None)

    def test_keys(self):
        user = User()
        self.assertIn("id", user.to_dict())
        self.assertIn("created_at", user.to_dict())
        self.assertIn("updated_at", user.to_dict())
        self.assertIn("__class__", user.to_dict())

    def test_output(self):
        time = datetime.today()
        user = User()
        user.id = "1234567890"
        user.created_at = user.updated_at = time
        dictionary = {
            'id': '1234567890',
            '__class__': 'User',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(user.to_dict(), dictionary)

if __name__ == "__main__":
    unittest.main()