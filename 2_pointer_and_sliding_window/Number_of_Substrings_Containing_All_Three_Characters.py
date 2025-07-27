class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        count = 0

        for i in range(n):
            freq = {'a':0, 'b':0, 'c':0}

            for j in range(i, n):

                if s[j] in 'abc':
                    freq[s[j]] = 1
                
                if freq['a'] + freq['b'] + freq['c'] == 3:
                    count += 1

        return count
    
obj = Solution()

s = "abcabc"

print(obj.numberOfSubstrings(s))