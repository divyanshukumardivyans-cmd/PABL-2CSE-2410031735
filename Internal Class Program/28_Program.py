#You are given a rectangular matrix mat[][] of size n x m, and your task is to return an array while traversing the matrix in spiral form.

def spiral_traversal(mat):
    result = []
    if not mat:
        return result

    top, bottom, left, right = 0, len(mat) - 1, 0, len(mat[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1

    return result
# Example usage:
mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiral_traversal(mat))