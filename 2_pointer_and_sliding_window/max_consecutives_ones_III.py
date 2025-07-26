class Solution:

    ## Brute force approach

    # def longestOnes(self, nums: list[int], k: int) -> int:
    #     n = len(nums)
    #     max_len = 0

    #     for i in range(n):
    #         zeros = 0

    #         for j in range(i, n):
    #             if nums[j] == 0:
    #                 zeros += 1

    #             if zeros <= k:
    #                 wLength = j - i + 1
    #                 max_len = max(max_len, wLength)

    #             else:
    #                 break

    #     return max_len


    
    ## Most optimal approach

    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        max_len = 0
        zeros = 0
        
        while r < n:
            
            if nums[r] == 0:
                zeros += 1

            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            if zeros <= k:
                window_length = r - l + 1
                max_len = max(max_len, window_length)

            r += 1
        
        return max_len
    
                


    
obj = Solution()

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

print(obj.longestOnes(nums,k))

        