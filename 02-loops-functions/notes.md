# Module 2 - Loops, functions

## for
- `range(stop)`, `range(start, stop)`, `range(start, stop, step)`
- start is included, stop is NOT: `range(2, 10)` goes 2..9
- `for ch in "hello"` loops over each character
- `for i in range(0, len(s), 2)` loops by index, every other char

## while
- same as other languages, just remember to update the counter or it never stops

## break / continue
- `break` leaves the loop completely
- `continue` skips the rest of this iteration and goes to the next one
- skipping multiples of 5 needs `continue`, `break` would end the loop at 5

## functions
- `def name(params):`, no return type
- `return` ends the function right there
- `if __name__ == "__main__": main()` runs main only when the file is run directly
- `s[::-1]` reverses a string
