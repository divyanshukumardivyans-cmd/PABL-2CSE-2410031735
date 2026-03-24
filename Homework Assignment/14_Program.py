#Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

def find_duplicate(nums):
    # Phase 1: Detect cycle
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]          # Move 1 step
        fast = nums[nums[fast]]    # Move 2 steps
        if slow == fast:
            break

    # Phase 2: Find entry point of cycle (duplicate)
    slow2 = nums[0]
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow
print(find_duplicate([1, 3, 4, 2, 2]))