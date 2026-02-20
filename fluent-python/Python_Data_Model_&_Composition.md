# Python Data Model & Composition

## 1. The Python Data Model

The **data model** is a set of rules that lets your custom classes hook into Python's built-in behavior. You do this by implementing **dunder (double underscore) methods** like `__len__`, `__getitem__`, `__repr__`, etc.

### Simple Example

```python
class Bag:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

bag = Bag(['apple', 'banana', 'cherry'])

len(bag)      # → 3         (calls __len__)
bag[0]        # → 'apple'   (calls __getitem__)
bag[1:]       # → ['banana', 'cherry']  (slicing, also __getitem__)

for item in bag:  # iteration works automatically!
    print(item)
```

By just adding two methods, Python now knows how to:
- get the length
- index and slice
- iterate (Python uses `__getitem__` under the hood if no `__iter__` exists)

> Think of dunder methods as **plugging your class into Python's socket**. Once plugged in, all the built-in features just work.

---

## 2. Composition

**Composition** means your class *contains* another object and uses it to do work, rather than inheriting from it.

### Inheritance vs Composition

**Inheritance** — your class *is* a list:
```python
class Bag(list):  # Bag inherits everything from list
    pass

bag = Bag(['apple', 'banana'])
bag.append('cherry')  # works, but now Bag is fully a list
bag.sort()            # also works — maybe you don't want this!
```

**Composition** — your class *has* a list:
```python
class Bag:
    def __init__(self, items):
        self._items = items  # contains a list internally

    def __len__(self):
        return len(self._items)  # delegates to the list

    def __getitem__(self, index):
        return self._items[index]  # delegates to the list
```

Now `Bag` uses the list's power, but only exposes what you choose to expose. You're in control.

---

## 3. Delegation

When composition *forwards* work to an inner object, that's called **delegation**.

```python
def __len__(self):
    return len(self._items)  # "I delegate this to my internal list"
```

`Bag` doesn't know how to count — it just asks `self._items` to do it.

---

## 4. How They Work Together (FrenchDeck example)

```python
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    def __init__(self):
        self._cards = [Card(rank, suit)      # composition: contains a list
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)              # delegates to list

    def __getitem__(self, position):
        return self._cards[position]         # delegates to list
```

Because of the **data model** (`__len__`, `__getitem__`), you get for free:
- `len(deck)` ✅
- `deck[0]` ✅
- `deck[-1]` ✅
- `random.choice(deck)` ✅
- `sorted(deck)` ✅
- `for card in deck` ✅

Because of **composition** (not inheritance), `FrenchDeck` doesn't accidentally expose `list.append()`, `list.remove()`, etc. — the deck stays clean.

---

## 5. Quick Summary

| Concept | What it means | Example |
|---|---|---|
| **Data model** | Dunder methods let your class work with Python's syntax | `__len__` makes `len()` work |
| **Composition** | Your class *contains* another object | `self._cards = []` |
| **Delegation** | Forward method calls to the inner object | `return len(self._cards)` |
| **Inheritance** | Your class *is* another object | `class Deck(list)` |

> **Rule of thumb:** Use composition when you want to *use* another class's behavior. Use inheritance when your class truly *is* a more specific version of another class.
