## Circular Left Shift of an Array in Python

## Overview

This project demonstrates how to perform a circular left shift on an array using Python. Instead of modifying the array while iterating through it, the program creates a temporary list, calculates each element's new position using modular arithmetic, and then updates the original array.

## Features

- Performs a circular left shift by n positions.
- Uses modular arithmetic to wrap elements around the array.
- Preserves the original array by using a temporary list during computation.
- Updates the original array efficiently using slice assignment.
- Handles invalid shift values ("n <= 0").

## How It Works

1. Determine the length of the array.
2. Create a temporary list of the same size.
3. For each element, calculate its new index using:
   (current_index - n) % length
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
- Algorithmic thinking

## Example

Input

Array: [10, 20, 30, 40, 12, 11]
Shift: 2

Output

[30, 40, 12, 11, 10, 20]

## Learning Outcome

This project strengthened my understanding of circular indexing, modulo operations, and how to manipulate arrays without overwriting elements during iteration. It also reinforced the importance of designing algorithms that are both clear and efficient.
