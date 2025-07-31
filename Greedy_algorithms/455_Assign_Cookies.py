class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:

        n = len(g)
        m = len(s)

        l, r = 0, 0

        g.sort()
        s.sort()

        while l < m and r < n:
            if s[l] >= g[r]:
                r += 1

            l += 1

        return r
    
g = [1,2]
s = [1,2,3]

obj = Solution()

print(obj.findContentChildren(g, s))
        