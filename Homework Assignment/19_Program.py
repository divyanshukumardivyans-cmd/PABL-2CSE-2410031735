#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

def is_subset(a, b):
    set_a = set(a)
    for element in b:
        if element not in set_a:
            return False
    return True
a = [1, 2, 3, 4, 5]
b = [2, 3, 4]
print(is_subset(a, b))