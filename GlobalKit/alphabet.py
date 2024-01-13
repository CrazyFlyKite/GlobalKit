from dataclasses import dataclass, field
from typing import Union

# Define new custom type: str or None
type StrOrNone = Union[str, None]


# Define Alphabet
@dataclass
class Alphabet:
	full_lowercase: str
	full_uppercase: str = field(init=False)
	full: str = field(init=False)

	vowels_lowercase: str
	vowels_uppercase: str = field(init=False)
	vowels: str = field(init=False)

	consonants_lowercase: str
	consonants_uppercase: str = field(init=False)
	consonants: str = field(init=False)

	special_lowercase: StrOrNone = None
	special_uppercase: StrOrNone = field(init=False)
	special: StrOrNone = field(init=False)
	has_special: bool = field(init=False)

	def __post_init__(self):
		self.full_uppercase = self.full_lowercase.upper()
		self.full = self.full_lowercase + self.full_uppercase

		self.vowels_uppercase = self.vowels_lowercase.upper()
		self.vowels = self.vowels_lowercase + self.vowels_uppercase

		self.consonants_uppercase = self.consonants_lowercase.upper()
		self.consonants = self.consonants_lowercase + self.consonants_uppercase

		if self.special_lowercase is not None:
			self.special_uppercase = self.special_lowercase.upper()
			self.special = self.special_lowercase + self.special_uppercase
			self.has_special = True
		else:
			self.special_uppercase = None
			self.special = None
			self.has_special = False
