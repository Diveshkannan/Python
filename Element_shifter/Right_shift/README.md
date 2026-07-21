## Circular Right Shift of an Array in Python

## Overview

This project demonstrates how to perform a circular right shift on an array using Python. The program creates a temporary list, calculates the new position of each element using modular arithmetic, and updates the original array after all elements have been repositioned.

## Features

- Performs a circular right shift by n positions.
- Uses modular arithmetic to wrap elements around the array.
- Prevents data loss by storing shifted elements in a temporary list.
- Updates the original array using slice assignment.
- Handles invalid shift values ("n <= 0").

## How It Works

1. Determine the length of the array.
2. Create a temporary list of the same size.
3. For each element, calculate its new index using:
   (current_index + n) % length
4. Place each element into its new position.
5. Copy the temporary list back into the original array.

## Time Complexity

- Time: O(n)
- Space: O(n)

## Concepts Practiced

- Functions
- Lists
- Modular arithmetic
- Circular indexing
- Array manipulation
- Slice assignment
- Algorithm design

## Example

Input

Array: [10, 20, 30, 40, 12, 11]
Shift: 2

Output

[12, 11, 10, 20, 30, 40]

## Learning Outcome

This project strengthened my understanding of circular array operations, modulo arithmetic, and index manipulation. It also reinforced the importance of using a temporary data structure to avoid overwriting elements during the shifting process and improved my ability to design clean and efficient algorithms.
