#Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix.

def median(mat):
    n, m = len(mat), len(mat[0])
    elements = []
    
    for i in range(n):
        for j in range(m):
            elements.append(mat[i][j])
    
    elements.sort()
    mid = (n * m) // 2
    return elements[mid]
# Example usage:
mat = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]
print(median(mat))