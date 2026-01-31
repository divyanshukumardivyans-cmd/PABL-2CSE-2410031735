#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
print(kth_smallest(arr, 4))
