from typing import Union, Self, Optional, Iterator

# Define new custom type: Str or None
type StrOrNone = Union[str, None]


# Define Alphabet
class Alphabet(object):
	def __init__(self, full: str, vowels: str, consonants: str, special: Optional[StrOrNone] = None) -> None:
		super().__init__()

		# Initialize the full alphabet
		self.full_lowercase: str = full.lower()
		self.full_uppercase: str = full.upper()
		self.full: str = self.full_lowercase + self.full_uppercase

		# Initialize the vowels
		self.vowels_lowercase: str = vowels.lower()
		self.vowels_uppercase: str = vowels.upper()
		self.vowels: str = self.vowels_lowercase + self.vowels_uppercase

		# Initialize the consonants
		self.consonants_lowercase: str = consonants.lower()
		self.consonants_uppercase: str = consonants.upper()
		self.consonants: str = self.consonants_lowercase + self.consonants_uppercase

		# Check if special characters are provided
		if special is None:
			self.special_lowercase: None = None
			self.special_uppercase: None = None
			self.special: None = None
			self.is_contains_special: bool = False
		else:
			# Initialize the special characters
			self.special_lowercase: str = special.lower()
			self.special_uppercase: str = special.upper()
			self.special: str = self.special_lowercase + self.special_uppercase
			self.is_contains_special: bool = True

	def __repr__(self) -> str:
		return self.full

	def __str__(self) -> str:
		return f'Alphabet: {self.full_lowercase}'

	def __call__(self, *args, **kwargs) -> None:
		# Print the full alphabet
		print('Full:\t\t', ' '.join(self.full_lowercase))
		print('-' * 100)

		# Print the vowels
		print('Vowels:\t\t', ' '.join(self.vowels_lowercase))

		# Print the consonants
		print('Consonants:\t', ' '.join(self.consonants_lowercase))

		# Check if special characters are provided
		if self.special is not None:
			print('Special:\t', ' '.join(self.special_lowercase))

	def __iter__(self) -> Iterator[str]:
		return iter(self.full_lowercase)

	def __getitem__(self, key: int) -> str:
		return self.full_lowercase[key]

	def __len__(self) -> int:
		return len(self.full_lowercase)

	def __lt__(self, other: Self) -> bool:
		return len(self.full_lowercase) < len(other.full_lowercase)

	def __gt__(self, other: Self) -> bool:
		return len(self.full_lowercase) > len(other.full_lowercase)

	def __eq__(self, other: Self) -> bool:
		return self.full_lowercase == other.full_lowercase

	def __ne__(self, other: Self) -> bool:
		return self.full_lowercase != other.full_lowercase

	def __le__(self, other: Self) -> bool:
		return len(self.full_lowercase) <= len(other.full_lowercase)

	def __ge__(self, other: Self) -> bool:
		return len(self.full_lowercase) >= len(other.full_lowercase)
