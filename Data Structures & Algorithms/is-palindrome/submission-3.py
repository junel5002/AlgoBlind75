class Solution:
    def isPalindrome(self, s: str) -> bool:
        
#for this question we will use two pointers

        #one pointer starting from the left and the other from the right
        #we will basically use them as indices

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower(): #we must convert all into lowercase
                return False
            l, r = l + 1, r - 1        #increment so it moves to the next character
        return True
    
    #the function below is to check whether 
    #the character c is alphanumeric; we use the ord() to get the ASCII number
    #so meaning that if ord(c) is in between any of those then it's alphanumeric
    
    def alphaNum(self, c): 
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9")
        )
