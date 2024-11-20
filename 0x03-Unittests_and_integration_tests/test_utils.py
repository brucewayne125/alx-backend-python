#!/usr/bin/env python3
#TestAccessNestedMap:- refers to the unittest for the access_nested_map function
#test_access_nested_map:- tests if the access_nested_map function returns the correct output
#@parameterized.expand:- used to test the input and output combinations

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2 ),
        ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        missingKey = context.exception.args[0]

        self.assertEqual(str(context.exception), repr(missingKey))

if __name__ == "__main__":
    unittest.main()
