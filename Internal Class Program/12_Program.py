#Given an array arr[] denoting heights of n towers and a positive integer k.

def get_min_diff(arr, k):
    n = len(arr)
    if n == 1:
        return 0
    
    arr.sort()
    
    # Initial max difference
    result = arr[-1] - arr[0]
    
    # Smallest and largest after first modification
    small = arr[0] + k
    big = arr[-1] - k

    # Swap if needed
    if small > big:
        small, big = big, small

    # Try modifying each tower as pivot
    for i in range(1, n - 1):
        subtract = arr[i] - k
        add = arr[i] + k
        
        # Ignore if subtract becomes negative
        if subtract < 0:
            continue
        
        # Update smallest
        current_small = min(small, subtract)
        # Update biggest
        current_big = max(big, add)

        result = min(result, current_big - current_small)

    return result
k = 2 
arr = [1, 5, 8, 10]
print(get_min_diff(arr, k))