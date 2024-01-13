from GlobalKit.alphabet import Alphabet

# Create instances of the Alphabet dataclass for many languages
english = Alphabet('abcdefghijklmnopqrstuvwxyz', 'aeiouy', 'bcdfghjklmnpqrstvwxz')
spanish = Alphabet('abcdefghijklmnñopqrstuvwxyz', 'aeiouáéíóúü', 'bcdfghjklmnñpqrstvwxyz')
french = Alphabet('abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüœ', 'aeiouàâéèêëîïôùûüœ', 'bcçdfghjklmnpqrstvwxyz')
german = Alphabet('abcdefghijklmnopqrstuvwxyzäöüß', 'aeiouäöü', 'bcdfghjklmnpqrstvwxyzß')
italian = Alphabet('abcdefghijklmnopqrstuvwxyzàèéìòù', 'aeiouàèéìòù', 'bcdfghjklmnpqrstvwxyz')
portuguese = Alphabet('abcdefghijklmnopqrstuvwxyzáâãàçéêíóôõú', 'aeiouáâãàéêíóôõú', 'bcdfghjklmnpqrstvwxyzç')
dutch = Alphabet('abcdefghijklmnopqrstuvwxyz', 'aeiou', 'bcdfghjklmnpqrstvwxyz')
finnish = Alphabet('abcdefghijklmnopqrstuvwxyzåäö', 'aeiouyåäö', 'bcdfghjklmnpqrstvwxz')
swedish = Alphabet('abcdefghijklmnopqrstuvwxyzåäö', 'aeiouyåäö', 'bcdfghjklmnpqrstvwxz')
norwegian = Alphabet('abcdefghijklmnopqrstuvwxyzåæø', 'aeiouyåæø', 'bcdfghjklmnpqrstvwxz')
russian = Alphabet('абвгдеёжзийклмнопрстуфхцчшщъыьэюя', 'аеёиоуэыюя', 'бвгджзйклмнпрстфхцчшщ', 'ъь')
ukrainian = Alphabet('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя', 'аеєиіїоуюя', 'бвгґджзйклмнпрстфхцчшщ', 'ь')
bulgarian = Alphabet('абвгдежзийклмнопрстуфхцчшщъьюя', 'аеиоуъя', 'бвгджзйклнпрстфхцчшщ', 'ь')
polish = Alphabet('aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż', 'aeiouyąę', 'bcćdfghjklłmnńpqrsśtvwxzźż')

# Define other character sets
digits: str = '0123456789'
brackets: str = '()[]{}<>'
space: str = ' '
newline: str = '\n'
tab: str = '\t'
