## leetcode 76. Minimum Window Substring

## brute force approach
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sIndex = -1
        count = 0
        minLength = float('inf')

        n = len(s)
        m = len(t)

        for i in range(n):
            count = 0
            hash = [0]*256

            for j in range(m):
                hash[ord(t[j])] += 1

            for j in range(i, n):
                if hash[ord(s[j])] > 0:
                    count += 1
                hash[ord(s[j])] -= 1

                if count == m:
                    if (j-i+1) < minLength:
                        minLength = j - i + 1
                        sIndex = i
                    break
        if sIndex == -1:
            return ""

        return s[sIndex : sIndex + minLength]

        
s = "ADOBECODEBANC"
t = "ABC"

obj = Solution()

print(obj.minWindow(s, t))