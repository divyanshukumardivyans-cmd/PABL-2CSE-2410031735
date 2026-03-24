#Given an array arr and a number k. One can apply a swap operation on the array any number of times, i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] . Find the minimum number of swaps required to bring all the numbers less than or equal to k together, i.e. make them a contiguous subarray.

def min_swaps(arr, k):
    count = sum(1 for x in arr if x <= k)
    bad = sum(1 for x in arr[:count] if x > k)
    
    min_swaps = bad
    for i in range(count, len(arr)):
        if arr[i] > k:
            bad += 1
        if arr[i - count] > k:
            bad -= 1
        min_swaps = min(min_swaps, bad)
    
    return min_swaps
arr = [2, 1, 5, 6, 3]
k = 3
print(min_swaps(arr, k))