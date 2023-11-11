#!/usr/bin/python3
"""Unittest for base_model

Unittest classes:
    TestBaseModel_instance
    TestBaseModel_saving
    TestBaseModel_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instance(unittest.TestCase):
    """Unisttest for instantiating class"""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_args_kwargs(self):
        time = datetime.today()
        time_formatted = time.isoformat()
        basemodel = BaseModel("12", id="345", created_at=time_formatted, updated_at=time_formatted)
        self.assertEqual(basemodel.id, "345")
        self.assertEqual(basemodel.created_at, time)
        self.assertEqual(basemodel.updated_at, time)


class TestBaseModel_saving(unittest.TestCase):
    """Unist test for saving class"""

    def test_save(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save1(self):
        basemodel = BaseModel()
        sleep(0.05)
        update1 = basemodel.updated_at
        basemodel.save()
        self.assertLess(update1, basemodel.updated_at)

    def test_update_file(self):
        basemodel = BaseModel()
        basemodel.save()
        id = "BaseModel." + basemodel.id
        with open("file.json", "r") as f:
            self.assertIn(id, f.read())


class TestBaseModel_dict(unittest.TestCase):
    """Unittest for to_dict"""

    def test_type(self):
        basemodel = BaseModel()
        self.assertTrue(dict, type(basemodel.to_dict()))

    def test_arg(self):
        basemodel  = BaseModel()
        with self.assertRaises(TypeError):
            basemodel .to_dict(None)

    def test_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_output(self):
        time = datetime.today()
        basemodel = BaseModel()
        basemodel.id = "1234567890"
        basemodel.created_at = basemodel.updated_at = time
        dictionary = {
            'id': '1234567890',
            '__class__': 'BaseModel',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(basemodel.to_dict(), dictionary)

if __name__ == "__main__":
    unittest.main()