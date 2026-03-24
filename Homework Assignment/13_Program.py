#You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.

def min_jumps(arr):
    n = len(arr)
    
    # If array has only one element → already at the end
    if n <= 1:
        return 0
    
    # If first element is 0 → we cannot move anywhere
    if arr[0] == 0:
        return -1

    # Initialize values
    maxReach = arr[0]
    steps = arr[0]
    jumps = 1  # We must take at least one jump from index 0

    for i in range(1, n):
        # If we reached the end
        if i == n - 1:
            return jumps

        # Update maxReach
        maxReach = max(maxReach, i + arr[i])

        # Use a step
        steps -= 1

        # When no more steps left → we must jump
        if steps == 0:
            jumps += 1

            # If we cannot move further
            if i >= maxReach:
                return -1

            # Reset the steps for the next jump window
            steps = maxReach - i

    return -1
print(min_jumps([2, 3, 1, 1, 4]))