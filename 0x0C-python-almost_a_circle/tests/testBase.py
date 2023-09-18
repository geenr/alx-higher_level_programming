#!/usr/bin/python3
"""Defining tests for the Base class."""


import unittest
import os
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """Unittest for testing the Base class."""

    def test_to_json_string(self):
