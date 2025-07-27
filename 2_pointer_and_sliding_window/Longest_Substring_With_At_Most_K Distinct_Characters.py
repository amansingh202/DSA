class Solution:
    def kDistinctChar(self, s, k):
        #your code goes here

        n = len(s)
        l = 0
        r = 0
        max_len = 0
        mpp = {}

        while r < n:
            mpp[s[r]] = mpp.get(s[r], 0) + 1

            if len(mpp) > k:
                mpp[s[l]] -= 1

                if mpp[s[l]] == 0:
                    del mpp[s[l]]

                l += 1

            if len(mpp) <= k:
                max_len = max(max_len, r - l + 1)

            r += 1

            

        return max_len
    
obj = Solution()

s = "aababbcaacc"
k = 2

print(obj.kDistinctChar(s, k))