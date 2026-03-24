#Given a number x and an array of integers arr, find the smallest subarray with sumgreater than the given value. If such a subarray do not exist return 0 in that case.

def smallest_subarray(arr, x):
    min_length = float('inf')
    current_sum = 0
    start = 0
    
    for end in range(len(arr)):
        current_sum += arr[end]
        
        while current_sum > x:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1
            
    return min_length if min_length != float('inf') else 0
arr = [1, 4, 45, 6, 0, 19]
x = 51
print(smallest_subarray(arr, x))