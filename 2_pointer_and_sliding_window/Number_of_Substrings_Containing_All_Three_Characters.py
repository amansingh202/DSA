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
    
    def numberOfSubstrings_mostOptimal(self, s: str) -> int:
        n = len(s)

        count = 0

        last_seen = {'a': -1, 'b': -1, 'c': -1}

        for i in range(n):
            if s[i] in last_seen:
                last_seen[s[i]] = i

            if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
                count += 1 + min(last_seen['a'], last_seen['b'], last_seen['c'])

        return count
                        



    
obj = Solution()

s = "abcabc"

print(obj.numberOfSubstrings_mostOptimal(s))