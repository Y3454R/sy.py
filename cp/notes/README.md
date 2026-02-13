# Python Array & Range Operations — Notes (DSA Focus)

This document summarizes techniques and mistakes discussed so far.

---

## 1️⃣ Printing a `map` Object

### ❌ Mistake

```python
print(map(int, input().split()))
```

Output:

```
<map object at 0x...>
```

### ✅ Fix

Convert to list:

```python
a = list(map(int, input().split()))
print(a)
```

### 💡 Why?

- `map()` returns an iterator in Python 3
- It must be consumed (e.g., using `list()`)

---

## 2️⃣ Sorting a List

### ❌ Mistake

```python
a_sorted = sort(a)
```

### 🔎 Problem

- `sort()` is a list method
- Not a standalone function

### ✅ Correct Ways

#### In-place sort

```python
a.sort()
```

#### Reverse sort

```python
a.sort(reverse=True)
```

#### Using `sorted()` (returns new list)

```python
a_sorted = sorted(a)
a_sorted = sorted(a, reverse=True)
```

### ⚠ Difference

| Method      | Modifies Original | Returns New List |
| ----------- | ----------------- | ---------------- |
| `a.sort()`  | Yes               | No (`None`)      |
| `sorted(a)` | No                | Yes              |

---

## 3️⃣ Sorting from Index l to r

Python has no direct partial sort.

### ✅ Technique

```python
a[l:r+1] = sorted(a[l:r+1])
```

### Reverse sort in range

```python
a[l:r+1] = sorted(a[l:r+1], reverse=True)
```

### ⏱ Complexity

If k = r - l + 1:

```
O(k log k)
```

---

## 4️⃣ Reversing from Index l to r

### ✅ Simple Pythonic Way

```python
a[l:r+1] = a[l:r+1][::-1]
```

Time complexity:

```
O(k)
```

---

### ✅ Interview-Friendly Two Pointer Method

```python
while l < r:
    a[l], a[r] = a[r], a[l]
    l += 1
    r -= 1
```

- Time: O(k)
- Space: O(1)
- Preferred in interviews

---

## 5️⃣ Printing an Array

### Default print

```python
print(a)
```

Output:

```
[1, 2, 3]
```

---

### Space-separated (Competitive Programming style)

```python
print(*a)
```

Output:

```
1 2 3
```

---

### One element per line

```python
for x in a:
    print(x)
```

---

## 6️⃣ Key DSA Takeaways

- Understand iterators vs lists (`map`, generators)
- Know difference between in-place vs returned copy
- Slicing creates a copy
- Two-pointer techniques are essential
- Prefer O(1) space when possible in interviews

---

## 🔥 Mental Model Summary

- `map()` → lazy iterator
- `sort()` → modifies list
- `sorted()` → returns new list
- `[::-1]` → reverse copy
- `a[l:r]` → always creates a new list

---

<!-- Keep extending this document as you learn more techniques and common mistakes. -->
