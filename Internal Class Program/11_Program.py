#Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]

arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr, k))