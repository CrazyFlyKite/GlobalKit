from typing import Final

from .alphabet import Alphabet

# Instances of the Alphabet dataclass
english: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyz', 'aeiouy', 'bcdfghjklmnpqrstvwxz')
spanish: Final[Alphabet] = Alphabet('abcdefghijklmnñopqrstuvwxyz', 'aeiouáéíóúü', 'bcdfghjklmnñpqrstvwxyz')
french: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüœ', 'aeiouàâéèêëîïôùûüœ', 'bcçdfghjklmnpqrstvwxyz')
german: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzäöüß', 'aeiouäöü', 'bcdfghjklmnpqrstvwxyzß')
italian: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzàèéìòù', 'aeiouàèéìòù', 'bcdfghjklmnpqrstvwxyz')
portuguese: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzáâãàçéêíóôõú', 'aeiouáâãàéêíóôõú', 'bcdfghjklmnpqrstvwxyzç')
dutch: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyz', 'aeiou', 'bcdfghjklmnpqrstvwxyz')
finnish: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzåäö', 'aeiouyåäö', 'bcdfghjklmnpqrstvwxz')
swedish: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzåäö', 'aeiouyåäö', 'bcdfghjklmnpqrstvwxz')
norwegian: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzåæø', 'aeiouyåæø', 'bcdfghjklmnpqrstvwxz')
russian: Final[Alphabet] = Alphabet('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'аеёиоуэыюя', 'бвгджзйклмнпрстфхцчшщ', 'ъь')
ukrainian: Final[Alphabet] = Alphabet('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя', 'аеєиіїоуюя', 'бвгґджзйклмнпрстфхцчшщ', 'ь')
bulgarian: Final[Alphabet] = Alphabet('абвгдежзийклмнопрстуфхцчшщъьюя', 'аеиоуъя', 'бвгджзйклнпрстфхцчшщ', 'ь')
polish: Final[Alphabet] = Alphabet('aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż', 'aeiouyąę', 'bcćdfghjklłmnńpqrsśtvwxzźż')

# Other character sets
digits: Final[str] = '0123456789'
brackets: Final[str] = '()[]{}<>'
space: Final[str] = ' '
newline: Final[str] = '\n'
tab: Final[str] = '\t'
