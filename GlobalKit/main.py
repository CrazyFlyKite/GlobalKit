from typing import Final

from .alphabet import Alphabet

# Alphabets
ENGLISH: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyz', 'aeiouy', 'bcdfghjklmnpqrstvwxz')
SPANISH: Final[Alphabet] = Alphabet('abcdefghijklmnñopqrstuvwxyz', 'aeiouáéíóúü', 'bcdfghjklmnñpqrstvwxyz')
FRENCH: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüœ', 'aeiouàâéèêëîïôùûüœ', 'bcçdfghjklmnpqrstvwxyz')
GERMAN: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzäöüß', 'aeiouäöü', 'bcdfghjklmnpqrstvwxyzß')
ITALIAN: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzàèéìòù', 'aeiouàèéìòù', 'bcdfghjklmnpqrstvwxyz')
PORTUGUESE: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzáâãàçéêíóôõú', 'aeiouáâãàéêíóôõú', 'bcdfghjklmnpqrstvwxyzç')
DUTCH: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyz', 'aeiou', 'bcdfghjklmnpqrstvwxyz')
FINNISH: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzåäö', 'aeiouyåäö', 'bcdfghjklmnpqrstvwxz')
SWEDISH: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzåäö', 'aeiouyåäö', 'bcdfghjklmnpqrstvwxz')
NORWEGIAN: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzåæø', 'aeiouyåæø', 'bcdfghjklmnpqrstvwxz')
RUSSIAN: Final[Alphabet] = Alphabet('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'аеёиоуэыюя', 'бвгджзйклмнпрстфхцчшщ', 'ъь')
UKRAINIAN: Final[Alphabet] = Alphabet('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя', 'аеєиіїоуюя', 'бвгґджзйклмнпрстфхцчшщ', 'ь')
BULGARIAN: Final[Alphabet] = Alphabet('абвгдежзийклмнопрстуфхцчшщъьюя', 'аеиоуъя', 'бвгджзйклнпрстфхцчшщ', 'ь')
POLISH: Final[Alphabet] = Alphabet('aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż', 'aeiouyąę', 'bcćdfghjklłmnńpqrsśtvwxzźż')

# Other
DIGITS: Final[str] = '0123456789'
BRACKETS: Final[str] = '()[]{}'
