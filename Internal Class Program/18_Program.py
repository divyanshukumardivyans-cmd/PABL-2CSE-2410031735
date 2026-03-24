#Given an integer n, find its factorial. Return a list of integers denoting the digitsthat make up the factorial of n.

def factorial_digits(n):
    result = [1]  # factorial starts as 1

    for x in range(2, n + 1):
        carry = 0

        # Multiply existing digits by x
        for i in range(len(result)):
            prod = result[i] * x + carry
            result[i] = prod % 10
            carry = prod // 10
        
        # Add remaining carry
        while carry:
            result.append(carry % 10)
            carry //= 10

    # Reverse to get correct digit order
    return result[::-1]
n = 5
print(factorial_digits(n))