class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #We will implement two pointers(L and R) for this question

        count = {}
        longest_length = 0

        L = 0
        

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R], 0)

            while (R - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            longest_length = max(longest_length, R - L + 1)

        return longest_length
