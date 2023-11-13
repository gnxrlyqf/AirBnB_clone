#!/usr/bin/python3
"""Unittest for review

Unittest classes:
    TestBaseModel_instance
    TestBaseModel_saving
    TestBaseModel_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instance(unittest.TestCase):
    """Unisttest for instantiating class"""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_args_kwargs(self):
        time = datetime.today()
        time_formatted = time.isoformat()
        review = Review("12", id="345", created_at=time_formatted, updated_at=time_formatted)
        self.assertEqual(review.id, "345")
        self.assertEqual(review.created_at, time)
        self.assertEqual(review.updated_at, time)

class TestReview_saving(unittest.TestCase):
    """Unist test for saving class"""

    def test_save(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save1(self):
        review = Review()
        sleep(0.05)
        update1 = review.updated_at
        review.save()
        self.assertLess(update1, review.updated_at)

    def test_update_file(self):
        review = Review()
        review.save()
        id = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(id, f.read())


class TestReview_dict(unittest.TestCase):
    """Unittest for to_dict"""

    def test_type(self):
        review = Review()
        self.assertTrue(dict, type(review.to_dict()))

    def test_arg(self):
        review = Review()
        with self.assertRaises(TypeError):
            review.to_dict(None)

    def test_keys(self):
        review = Review()
        self.assertIn("id", review.to_dict())
        self.assertIn("created_at", review.to_dict())
        self.assertIn("updated_at", review.to_dict())
        self.assertIn("__class__", review.to_dict())

    def test_output(self):
        time = datetime.today()
        review = Review()
        review.id = "1234567890"
        review.created_at = review.updated_at = time
        dictionary = {
            'id': '1234567890',
            '__class__': 'Review',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(review.to_dict(), dictionary)

if __name__ == "__main__":
    unittest.main()