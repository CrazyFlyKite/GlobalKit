# GlobalKit

[![License](https://img.shields.io/badge/License-MIT-green)](license.txt)

## Introduction

**GlobalKit** provides alphabets from various languages in different scripts.
It can be used for language-related tasks, educational purposes and more.
___

## Usage

### Alphabets

**GlobalKit** contains **lots** of alphabets (of type `Alphabet`) in supported languages:

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

All languages in GlobalKit are instances of the `Alphabet` class, providing a rich set of functionalities:

- **String Representation**
	- `str(english)`, `repr(english)`, …

- **Callable**:
	- `english()`, …

- **Iterator**:
	- `list(english)`, …

- **Length**:
	- `len(english)`, …

- **Get Item**:
	- `english[0]`, …

- **Comparisons:**:
	- `<`, `>`, `==`, `!=`, `<=`, `>=`

### String Manipulation

`check(string, *alphabets)` checks if `string` is present in any of the specified `*alphabets`.
The `*alphabets` must be of type `Alphabet`. The variables of this type can be imported from **GlobalKit**.

`is_contains_spaces(string)` checks if `string` contains any spaces.

`is_contains_numbers(string)` checks if `string` contains any numbers.

`is_contains_alphabetic(string)` checks if `string` contains any alphabetic letters.

`is_contains_lowercase(string)` checks if `string` contains any lowercase letters.

`is_contains_uppercase(string)` checks if `string` contains any uppercase letters.

`is_contains_special(string)` checks if `string` contains any special characters.

`is_contains_substring(string, substring)` checks if `string` contains `substring`.

#### Examples

```python
import GlobalKit as gk

print(gk.english.full)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(gk.french.full_lowercase)  # abcdefghijklmnopqrstuvwxyzàâçéèêëîïôùûüœ
print(gk.spanish.consonants_uppercase)  # BCDFGHJKLMNÑPQRSTVWXYZ
print(gk.german.vowels)  # aeiouäöüAEIOUÄÖÜ

print(gk.digits)  # 0123456789
print(gk.brackets)  # ()[]{}<>
print(gk.space)  #  

print(gk.dutch.special_lowercase)  # None
print(gk.russian.special_uppercase)  # ЪЬ
```

```python
from GlobalKit import english, french, russian, polish

print(english)  # Alphabet: abcdefghijklmnopqrstuvwxyz
print(repr(english))  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(list(english))  # ['a', 'b', 'c', …]
print(english[0])  # a
print(len(english))  # 26
english()  # Full:		 a b c …

print(russian > english)  # True
print(english < french)  # True
print(english == russian)  # False
print(english != polish)  # True
print(english >= russian)  # False
print(english <= french)  # True
```

```python
from GlobalKit import check, english, russian, digits

check('e', english)  # True
check('1', english, digits)  # True
check('h', russian.vowels)  # False
```

```python
from GlobalKit import is_contains_spaces, is_contains_uppercase, is_contains_special, is_contains_substring

is_contains_spaces('Hello, world!')  # True
is_contains_uppercase('hello, world!')  # False
is_contains_special('Hello, world!')  # True
is_contains_substring('Hello, world!', 'world')  # True
```

___

## Contact

- [Discord](https://discord.com/users/873920068571000833)
- [Email](mailto:karpenkoartem2846@gmail.com)
- [GitHub](https://github.com/CrazyFlyKite)
