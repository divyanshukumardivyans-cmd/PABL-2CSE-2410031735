#You are given two arrays a[] and b[], return the Union of both the arrays in any order.

def union_arrays(a, b):
    return list(set(a) | set(b))

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(sorted(union_arrays(a, b)))

