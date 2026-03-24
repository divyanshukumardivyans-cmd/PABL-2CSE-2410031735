#Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.

def has_triplet(arr, target):
    n = len(arr)
    arr.sort()  # Sort the array first

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return False

# Example usage:
arr = [1, 4, 45, 6, 10, 8]
target = 22
print(has_triplet(arr, target))