# Module 3 - Basic data structures

## list
- mutable, keeps order, index starts at 0
- `append(x)` adds at the end, `insert(i, x)` adds at a position
- `remove(x)` removes by value, `pop()` removes the last one (or `pop(i)`)
- `sort()`, `len()`, `",".join(list_of_strings)`
- list of lists: `lists[1][0]`

## tuple
- like a list but immutable, `x.append(4)` gives an error
- `x + (4, 5)` works because it creates a new tuple
- unpacking: `first, last, age = ("Jane", "Doe", 21)`
- unpacking needs the same number of values or it errors

## set
- no duplicates: `{1, 2, 2, 1}` -> `{1, 2}`
- `add()` instead of append
- can't hold mutable things like lists
- `set(my_list)` is an easy way to remove duplicates
- order doesn't matter when comparing: `{1,2,3} == {3,2,1}` is True
- (the course says sets are sorted, but that's only how small ints show up, sets have no order)

## dict
- key/value pairs, `d["key"]`
- reading a missing key -> KeyError, but `d["new"] = 1` just creates it
- keys must be immutable: string, number, tuple ok, list not ok
- `keys()`, `values()`, `items()`
