#!/usr/bin/python3
"""this is the test file for the 'Rectangle' class"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """here are the unit tests for 'Rectangle'"""

    def test_rectangle_default_initialisation(self):
        rectangle = Rectangle(1, 2)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertTrue(isinstance(rectangle, Rectangle))

    def test_rectangle_full_initialisation(self):
        rectangle = Rectangle(1, 2, 1, 7, 9)
        self.assertEqual(rectangle.height, 2)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 7)
        self.assertEqual(rectangle.id, 9)

    def test_rectangle_missing_width(self):
        with self.assertRaises(TypeError):
            Rectangle(height=1)

    def test_rectangle_missing_height(self):
        with self.assertRaises(TypeError):
            Rectangle(width=1)

    def test_rectangle_wrong_type_width(self):
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_rectangle_wrong_type_height(self):
        with self.assertRaises(TypeError):
            Rectangle(1, str)

    def test_rectangle_wrong_type_x(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [])

    def test_rectangle_wrong_type_y(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {})

    def test_rectangle_wrong_value_height(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_wrong_value_width(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_rectangle_wrong_value_x(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

    def test_rectangle_wrong_value_y(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 1, 1, -2)

    def test_rectangle_area(self):
        rectangle = Rectangle(3, 2)
        self.assertEqual(6, rectangle.area())

    def test_rectangle_display(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Rectangle(1, 2, 1, 1).display()
            self.assertEqual(fake_out.getvalue(), "\n #\n #\n")

    def test_rectangle_print(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
            self.assertEqual(fake_out.getvalue(), "[Rectangle] (12) 2/1 - 4/6\n")

    def test_rectangle_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_update_args(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(98, 19, 2, 3, 4)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 19)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_rectangle_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(y=1, width=2, x=3, id=89, height=30)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.height, 30)
        self.assertEqual(r1.width, 2)

    def test_rectangle_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        dictionary = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertEqual(r1_dictionary, dictionary)
