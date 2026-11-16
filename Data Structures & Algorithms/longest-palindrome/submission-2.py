class Solution:
    def longestPalindrome(self, s: str) -> int:
        

        char_freq = defaultdict(int)

        longest = 0

        for char in s:

            char_freq[char] += 1
 
            if char_freq[char] % 2 == 0:
                longest += 2

        for c in char_freq.values():
            if c % 2 == 1:
                longest += 1
                break
        
        return longest