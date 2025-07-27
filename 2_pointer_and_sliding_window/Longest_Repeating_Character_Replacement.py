class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            max_f = 0
            freq = [0]*26

            for j in range(i, n):
                index = ord(s[j])- ord('A')

                freq[index] += 1

                max_f = max(max_f, freq[index])

                changes = j - i + 1 - max_f

                if changes <= k:
                    max_len = max(max_f, j - i + 1)

        return max_len
    
    ## better approach
    
    def characterReplacement_better(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        l = 0
        r = 0
        freq = [0]*26
        max_f = 0

        while r < n:
            index = ord(s[r]) - ord('A')
            freq[index] += 1
            max_f = max(max_f, freq[index])

            while ( (r - l + 1) - max_f )> k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
    
    ## most optimal approach

    def characterReplacement_mostOptimal(self, s: str, k: int) -> int:
        n = len(s)
        max_len = 0
        l = 0
        r = 0
        freq = [0]*26
        max_f = 0

        while r < n:
            index = ord(s[r]) - ord('A')
            freq[index] += 1
            max_f = max(max_f, freq[index])

            if ( (r - l + 1) - max_f )> k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1

            if (r - l + 1) - max_f <= k:
                max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
    
    
    
    
    


    
obj = Solution()

s = "AABABBA"
k = 1

print(obj.characterReplacement_mostOptimal(s, k))