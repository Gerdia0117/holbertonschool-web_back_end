# Python - Variable Annotations

This project covers type annotations in Python 3.

## Tasks

### 0. Basic annotations - add
Write a type-annotated function `add` that takes two floats and returns their sum as a float.

## Requirements

- Python 3.7+
- All files must be executable
- All files must pass pycodestyle

## Usage

```python
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22))  # Output: 3.33
print(add.__annotations__)  # Output: {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```
