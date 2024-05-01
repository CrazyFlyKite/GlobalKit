# GlobalKit

[![License](https://img.shields.io/badge/License-MIT-green)](license.txt)

## Introduction

**GlobalKit** provides alphabets from various languages in different scripts.
It can be used for language-related tasks, educational purposes and more.

## Alphabets

**GlobalKit** contains **lots** of alphabets in supported languages:

- **English**
- **Spanish**
- **French**
- **Dutch**
- **Portuguese**
- **Italian**
- **Finnish**
- **Swedish**
- **Norwegian**
- **Russian**
- **Ukrainian**
- **Polish**
- **Bulgarian**
- **digits**
- and **many more**

All languages are instances of the `Alphabet` dataclass, providing access to various string representations:

- `full`, `full_lowercase`, `full_uppercase`
- `vowels`, `vowels_lowercase`, `vowels_uppercase`
- `consonants`, `consonants_lowercase`, `consonants_uppercase`
- `special`, `special_lowercase`, `special_uppercase`

To verify the presence of special characters in a language, you can use:

- `has_special`

If False, `special`, `special_lowercase`, `special_uppercase` will return `None`.

```python
import GlobalKit as gk

print(gk.english.full)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(gk.french.full_lowercase)  # abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüœ
print(gk.spanish.consonants_uppercase)  # BCDFGHJKLMNÑPQRSTVWXYZ
print(gk.german.vowels)  # aeiouäöüAEIOUÄÖÜ

print(gk.digits)  # 0123456789
print(gk.brackets)  # ()[]{}<>
print(gk.space)  # 

print(gk.dutch.special)  # None
print(gk.russian.special_uppercase)  # ЪЬ
print(gk.ukrainian.has_special)  # True
```

### Creating Your Own Alphabet

You can also easily create your custom alphabet using the `Alphabet` dataclass.
If the language unique characters beyond traditional vowels or consonants, you can specify them separately at the end.

```python
from typing import Final

from GlobalKit import Alphabet

romanian: Final[Alphabet] = Alphabet('abcdefghijklmnopqrstuvwxyzăâîșț', 'aeiouyăâî', 'bcdfghjklmnpqrstvwxzșț')

print(romanian.full)  # abcdefghijklmnopqrstuvwxyzăâîșțABCDEFGHIJKLMNOPQRSTUVWXYZĂÂÎȘȚ
```

## String Manipulations

`check(string, *alphabets)` checks if `string` is present in any of the specified `*alphabets`.
The `*alphabets` must be of type `Alphabet`. The variables of this type can be also imported from **GlobalKit**.

`is_contains_spaces(string)` checks if `string` contains any spaces.

`is_contains_numbers(string)` checks if `string` contains any numbers.

`is_contains_alphabetic(string)` checks if `string` contains any alphabetic letters.

`is_contains_lowercase(string)` checks if `string` contains any lowercase letters.

`is_contains_uppercase(string)` checks if `string` contains any uppercase letters.

`is_contains_special(string)` checks if `string` contains any special characters.

```python
from GlobalKit import check, english, russian, italian, ukrainian

print(check('e', english))  # True
print(check('1', english, italian))  # False
print(check('h', russian, ukrainian))  # False
```

```python
from GlobalKit import is_contains_spaces, is_contains_uppercase, is_contains_special

print(is_contains_spaces('Hello, world!'))  # True
print(is_contains_uppercase('hello, world!'))  # False
print(is_contains_special('Hello, world!'))  # True
```

## Contact

- [Discord](https://discord.com/users/873920068571000833)
- [GitHub](https://github.com/CrazyFlyKite)
- [Email](mailto:karpenkoartem2846@gmail.com)
