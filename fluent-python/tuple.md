# Tuples

A tuple is an immutable list — ordered, but cannot be changed after creation.

```python
my_list  = [1, 2, 3]
my_tuple = (1, 2, 3)

my_list[0]  = 99  # works
my_tuple[0] = 99  # TypeError!
```

Use a tuple when data is fixed and shouldn't change — coordinates, RGB colors, etc. The immutability signals to anyone reading the code: "this data is not meant to be modified."

## Initializing

```python
empty_tuple  = ()
empty_list   = []
empty_dict   = {}
```

## The single-item quirk

```python
not_a_tuple  = (1)   # Python sees this as just the number 1
actual_tuple = (1,)  # trailing comma makes it a tuple

type((1))   # → int
type((1,))  # → tuple
```

The trailing comma is what makes it a tuple, not the parentheses.

## With a generator expression

```python
tuple(ord(c) for c in 'ABC')  # → (65, 66, 67)
```

You can pass a genexp directly into `tuple()` — no extra parentheses needed.
