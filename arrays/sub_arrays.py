def subArrays(arr):
    n = len(arr)
    res = []

    for i in range(n):
        for j in range(i, n):
            res.append(arr[i:j+1])

    return res



arr = [2, 5, 1, 7, 10]
print(subArrays(arr))