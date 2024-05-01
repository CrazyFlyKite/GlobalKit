import unittest

from GlobalKit.functions import *
from GlobalKit.main import english, russian


class TestFunctions(unittest.TestCase):
	def test_check(self):
		self.assertEqual(check('a', english, russian), True)
		self.assertEqual(check('A', english), True)
		self.assertEqual(check('b', russian), False)

	def test_is_contains_spaces(self):
		self.assertEqual(is_contains_spaces('Hello, world!'), True)
		self.assertEqual(is_contains_spaces('Hello!'), False)

	def test_is_contains_alphabetic(self):
		self.assertEqual(is_contains_alphabetic('The world.'), True)
		self.assertEqual(is_contains_alphabetic('12345'), False)

	def test_is_contains_digits(self):
		self.assertEqual(is_contains_digits('12345'), True)
		self.assertEqual(is_contains_digits('Ten coins.'), False)

	def test_is_contains_lowercase(self):
		self.assertEqual(is_contains_lowercase('Hello, world!'), True)
		self.assertEqual(is_contains_lowercase('TOKEN N1'), False)

	def test_is_contains_uppercase(self):
		self.assertEqual(is_contains_uppercase('Hello, world!'), True)
		self.assertEqual(is_contains_uppercase('i have a banana.'), False)

	def test_is_contains_special(self):
		self.assertEqual(is_contains_special('So, what?'), True)
		self.assertEqual(is_contains_special('hello world'), False)


if __name__ == '__main__':
	unittest.main()
