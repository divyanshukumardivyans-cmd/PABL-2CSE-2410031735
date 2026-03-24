#You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order. Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.

def row_with_max_ones(arr):
    max_ones = 0
    row_index = -1
    
    for i in range(len(arr)):
        count_ones = sum(arr[i])
        
        if count_ones > max_ones:
            max_ones = count_ones
            row_index = i
            
    return row_index
arr = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [0, 0, 0, 0],
       [1, 1, 1, 1]]
print(row_with_max_ones(arr))