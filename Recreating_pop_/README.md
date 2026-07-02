# Recreating Python's `pop()` Function from Scratch

## Overview

This project recreates Python's built-in `list.pop()` function entirely from scratch without using `pop()` itself.

The goal of the project was not to replace Python's implementation, but to understand the internal logic behind element removal, list reconstruction, index handling, and mutable list modification.

Instead of relying on built-in list operations, the program manually removes an element, rebuilds the remaining list, and updates the original list object.

---

## Features

- Written entirely in Python
- Manual implementation of Python's `pop()` behavior
- Interactive command-line interface
- Supports removing the last element by default
- Supports removing an element at a user-specified index
- Handles invalid indices safely
- Rebuilds the list without using Python's `pop()`
- Preserves and returns the removed value
- Demonstrates mutable list modification using slice assignment
- Designed as an educational exploration of Python internals

---

## Implementation Concept

The program follows these steps:

1. Determine the current length of the list.
2. Validate the requested index.
3. Store the value that will be removed.
4. Create a temporary list with one fewer element.
5. Copy every element except the removed one into the temporary list.
6. Replace the contents of the original list using slice assignment.
7. Return the removed element.

---

## Example

Input

Length of your list:
5

Elements:
1
2
3
4
5

Index:
2

Output

Removed value:
3

Changed list:
[1, 2, 4, 5]

---

## Learning Objectives

This project helped me explore:

- Mutable vs immutable objects
- List reconstruction
- Slice assignment
- Manual memory-style thinking
- Index validation
- Algorithmic implementation of built-in functions
- Breaking down high-level Python features into low-level logic

---

## Future Improvements

- Remove the dependency on externally passing the list length.
- Eliminate reliance on the global list variable by modifying only the passed list reference.
- Support additional edge cases and more Python-like error handling.
- Compare performance against Python's built-in implementation.

---

## Author's Note

Built as part of my journey to understand programming beyond simply using built-in functions. Rather than calling Python's `pop()`, I wanted to understand how such a function could be implemented manually. This project strengthened my understanding of list manipulation, mutable objects, and algorithmic thinking through hands-on experimentation.