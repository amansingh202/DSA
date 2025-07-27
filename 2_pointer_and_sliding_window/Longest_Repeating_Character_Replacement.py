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
    
obj = Solution()

s = "AABABBA"
k = 1

print(obj.characterReplacement(s, k))