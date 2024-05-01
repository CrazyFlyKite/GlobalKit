from .alphabet import Alphabet


def check(string: str, *alphabets: Alphabet) -> bool:
	"""
	Check if a string is present in any of the specified alphabets.

	:parameter string: The string to be checked.
	:parameter alphabets: One or more alphabets as variable arguments.

	:returns: True if the string is found in any of the alphabets, False otherwise.
	"""

	return any(string in alphabet.full for alphabet in alphabets)


def is_contains_spaces(string: str) -> bool:
	"""
	Check if a string contains any space characters.

	:parameter string: The string to be checked.

	:returns: True if the string contains spaces, False otherwise.
	"""

	return any(character.isspace() for character in string)


def is_contains_alphabetic(string: str) -> bool:
	"""
	Check if a string contains any alphabetic characters.

	:parameter string: The string to be checked.

	:returns: True if the string contains alphabetic characters, False otherwise.
	"""

	return any(character.isalpha() for character in string)


def is_contains_digits(string: str) -> bool:
	"""
	Check if a string contains any numeric digits.

	:parameter string: The string to be checked.

	:returns: True if the string contains numeric digits, False otherwise.
	"""

	return any(character.isdigit() for character in string)


def is_contains_lowercase(string: str) -> bool:
	"""
	Check if a string contains any lowercase letters.

	:parameter string: The string to be checked.

	:returns: True if the string contains lowercase letters, False otherwise.
	"""

	return any(character.islower() for character in string)


def is_contains_uppercase(string: str) -> bool:
	"""
	Check if a string contains any uppercase letters.

	:parameter string: The string to be checked.

	:returns: True if the string contains uppercase letters, False otherwise.
	"""

	return any(character.isupper() for character in string)


def is_contains_special(string: str) -> bool:
	"""
	Check if a string contains any special characters.

	:parameter string: The string to be checked.

	:returns: True if the string contains special characters, False otherwise.
	"""

	return any(not (character.isalpha() or character.isspace()) for character in string)
