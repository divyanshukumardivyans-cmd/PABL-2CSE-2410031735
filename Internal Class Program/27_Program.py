#Given an array arr[] of integers, calculate the median.

def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    else:
        return arr[n // 2]
arr = [3, 1, 2, 5, 4]
print(median(arr))