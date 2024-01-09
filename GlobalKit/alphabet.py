from typing import Optional

# Define new type: Str or None
type StrOrNone = str | None

# Define Alphabet
class Alphabet:
	def __init__(self, full: str, vowels: str, consonants: str, special: Optional[StrOrNone] = None) -> None:
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
		else:
			# Initialize the special characters
			self.special_lowercase: str = special.lower()
			self.special_uppercase: str = special.upper()
			self.special: str = self.special_lowercase + self.special_uppercase

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
