# Module 1 - Variables, operations, conditions

## Variables
- names are case-sensitive: `Height` and `height` are different
- must start with a letter or `_`, never a number
- can't use keywords (`class`, `global`, `finally`...)
- no type declaration, Python figures it out
- `type(x)` shows the type

## Converting types
- `int()`, `float()`, `str()`
- `int(10.9)` -> `10` (cuts, doesn't round)
- `"hello" + 5` -> TypeError, need `"hello" + str(5)`

## Operators
- `/` always gives float: `36/4` -> `9.0`
- `//` integer division: `10//3` -> `3`
- `%` remainder: `10%3` -> `1`
- `**` power: `5**2` -> `25`
- `"foo" * 3` -> `"foofoofoo"`
- comparisons return bool. `5 == 5.0` is True
- strings compare alphabetically: `"cat" < "dog"` is True

## if / elif / else
- the first true condition wins, the rest is skipped, so order matters
- parentheses around the condition are optional
- the course says Python has no switch and uses a dict + `.get(key, default)` instead
  (Python 3.10 added `match`, but the course is older)
