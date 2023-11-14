#!/usr/bin/python3
"""Unittest for state

Unittest classes:
    TestState_instance
    TestState_saving
    TestState_dict
"""
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instance(unittest.TestCase):
    """Unisttest for instantiating class"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id(self):
        self.assertEqual(str, type(State().id))

    def test_created_at(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_args_kwargs(self):
        time = datetime.today()
        time_formatted = time.isoformat()
        state = State("12", id="345", created_at=time_formatted, updated_at=time_formatted)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, time)
        self.assertEqual(state.updated_at, time)

    def test_state(self):
        state = State()
        self.assertEqual(state.name, str)

class TestState_saving(unittest.TestCase):
    """Unist test for saving class"""

    def test_save(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)

    def test_save1(self):
        state = State()
        sleep(0.05)
        update1 = state.updated_at
        state.save()
        self.assertLess(update1, state.updated_at)

    def test_update_file(self):
        state = State()
        state.save()
        id = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(id, f.read())


class TestState_dict(unittest.TestCase):
    """Unittest for to_dict"""

    def test_type(self):
        state = State()
        self.assertTrue(dict, type(state.to_dict()))

    def test_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)

    def test_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_output(self):
        time = datetime.today()
        state = State()
        state.id = "1234567890"
        state.created_at = state.updated_at = time
        dictionary = {
            'id': '1234567890',
            '__class__': 'State',
            'created_at': time.isoformat(),
            'updated_at': time.isoformat()
        }
        self.assertDictEqual(state.to_dict(), dictionary)

if __name__ == "__main__":
    unittest.main()