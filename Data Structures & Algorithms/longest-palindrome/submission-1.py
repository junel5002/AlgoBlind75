class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)

        res = 0

        for char in s:
            count[char] += 1
            if count[char] % 2 == 0:
                res += 2

        for cnt in count.values():
            if cnt % 2:
                res += 1 
                break
        
        return res
            
        

