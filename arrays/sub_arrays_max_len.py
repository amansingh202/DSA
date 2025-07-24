def subarrays_max_len(arr, k):
    n = len(arr)
    max_len = 0

    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += arr[j]

            if sum <= k:
                max_len = max(max_len, j - i + 1)
    
    return max_len

arr = [2, 5, 1, 7, 10]

print(subarrays_max_len(arr,14))
