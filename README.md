
# GlobalKit

[![License](https://img.shields.io/badge/License-MIT-green)](license.txt)

## Introduction
**GlobalKit** is a module that provides alphabets from various languages in different scripts.
It can be used for language-related tasks, educational purposes and more.
___

## How to use
**GlobalKit** contains **lots** of alphabets (strings) in these supported languages:
**English**, **Spanish**, **French**, **Dutch**, **Portuguese**, **Italian**, **Finnish** , **Swedish**,
**Norwegian**, **Russian**, **Ukrainian**, **Polish**, **Bulgarian**, **digits** and **many more**

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

print(gk.english.full) # Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
```

```python
from GlobalKit import check, english, russian, digits

result1: bool = check('e', english)
result2: bool = check('1', english, digits)
result3: bool = check('h', russian.vowels)

print(result1)  # Output: True
print(result2)  # Output: True
print(result3)  # Output: False
```

```python
from GlobalKit import is_contains_spaces, is_contains_uppercase, is_contains_special, is_contains_substring

result1: bool = is_contains_spaces('Hello, world!')
result2: bool = is_contains_uppercase('hello, world!')
result3: bool = is_contains_special('Hello, world!')
result4: bool = is_contains_substring('Hello, world!', 'world')

print(result1)  # Output: True
print(result2)  # Output: False
print(result3)  # Output: True
print(result4)  # Output: True
```
___

## Contact
- [Discord](https://discord.com/users/873920068571000833)
- [Email](mailto:karpenkoartem2846@gmail.com)
- [GitHub](https://github.com/CrazyFlyKite)
