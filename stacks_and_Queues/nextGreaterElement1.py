class Solution:
    def nge1(self, nums1, nums2):

        n = len(nums2)
        arr = [-1]*n
        stack = []

        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                arr[i] = -1
            else:
                arr[i] = stack[-1]

            stack.append(nums2[i])

        arr_map = {nums2[i] : arr[i] for i in range(n)}

        return [arr_map[num] for num in nums1]

    
obj  = Solution()

nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(obj.nge1(nums1, nums2))