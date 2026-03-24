#Given three sorted arrays in non-decreasing order, print all common elements in non-decreasing order across these arrays. If there are no such elements return an empty array. In this case, the output will be -1.

def find_common_elements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    common = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j += 1
        else:
            k += 1

    return common if common else [-1]

# Example usage:
arr1 = [1, 5, 5]
arr2 = [2, 3, 5]
arr3 = [5, 5, 7]
print(find_common_elements(arr1, arr2, arr3))