#Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped betweenthe blocks during the rainy season.

def trap_water(arr):
    if not arr:
        return 0
    
    left, right = 0, len(arr) - 1
    left_max, right_max = arr[left], arr[right]
    water_trapped = 0
    
    while left < right:
        if arr[left] < arr[right]:
            left += 1
            left_max = max(left_max, arr[left])
            water_trapped += max(0, left_max - arr[left])
        else:
            right -= 1
            right_max = max(right_max, arr[right])
            water_trapped += max(0, right_max - arr[right])
    
    return water_trapped
print(trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))