#!/usr/bin/env python3
"""0. Parameterize a unit test"""

from unittest import TestCase, mock
from utils import access_nested_map, get_json
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(TestCase):
    """Test cases for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        """Test method for access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """Test if function raises a KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Test cases for get_json function"""

    def test_get_json(self):
        """Test that utils.get_json returns the expected result"""
        with mock.patch('utils.requests.get') as mock_request:
            test_url = "http://example.com"
            test_payload = {"payload": True}

            my_mock_response = mock.Mock(status_code=200)
            my_mock_response.json.return_value = test_payload
            mock_request.return_value = my_mock_response

            func_response = get_json(test_url)
            mock_request.assert_called_once_with(test_url)
            self.assertEqual(func_response, test_payload)

        with mock.patch('utils.requests.get') as mock_request:
            test_url = "http://holberton.io"
            test_payload = {"payload": False}

            my_mock_response = mock.Mock(status_code=200)
            my_mock_response.json.return_value = test_payload
            mock_request.return_value = my_mock_response

            func_response = get_json(test_url)
            mock_request.assert_called_once_with(test_url)
            self.assertEqual(func_response, test_payload)
