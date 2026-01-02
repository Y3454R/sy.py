# shallow_copy_demo.py

import copy

print("=== ORIGINAL LIST ===")
a = [[1, 2], [3, 4]]
print("a =", a)
print("id(a) =", id(a))
print()

print("=== SHALLOW COPY ===")
b = a.copy()
print("b =", b)
print("id(b) =", id(b))
print("a is b:", a is b)
print("a[0] is b[0]:", a[0] is b[0])
print()

print("=== MODIFY INNER LIST (b[0].append(99)) ===")
b[0].append(99)
print("a =", a)
print("b =", b)
print()

print("=== MODIFY OUTER LIST (b.append([5, 6])) ===")
b.append([5, 6])
print("a =", a)
print("b =", b)
print()

print("=== DEEP COPY ===")
c = copy.deepcopy(a)
print("c =", c)
print("a[0] is c[0]:", a[0] is c[0])
print()

print("=== MODIFY INNER LIST IN DEEP COPY (c[0].append(777)) ===")
c[0].append(777)
print("a =", a)
print("c =", c)

