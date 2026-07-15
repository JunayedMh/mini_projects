# Caesar Cipher

## The Goal: A Caesar cipher shifts every letter in a string by a fixed number of positions down the alphabet. Write a function that takes a string and a shift number, then returns the encrypted text.

- Input example: "abc", shift = 2

- Expected Output: "cde"

# The Twist:

1. It should only shift letters (leave punctuation and spaces exactly as they are).
2. It needs to "wrap around" the alphabet. If you shift 'z' by 1, it should become 'a'.
