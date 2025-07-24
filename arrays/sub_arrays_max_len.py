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

#print(subarrays_max_len(arr,14))


#Using 2 pointer and sliding window:-

def two_pointer_subarray(arr, k):
    n = len(arr)
    l = 0
    r = 0
    max_sum = 0
    max_len = 0

    while (r < n):
        max_sum += arr[r]

        while max_sum > k:
            max_sum -= arr[l]
            l += 1
        
        if max_sum < k:
            max_len = max(max_len, r - l + 1)
        
        r += 1
    return max_len

k = 14

print(two_pointer_subarray(arr, k))
