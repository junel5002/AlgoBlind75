'''
1. it's case insensitive, meaning 
you A --> a

2. we should ignore all non- alpha numeric charcters
(a-z, A-Z, and numbers 0-9)
we can compare such


s = "Was it a car or a cat I saw?"

after we ignore all the non alpha numeric characters

WasitacaroracatIsaw
        8 ^^

W ==  w

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0

        r = len(s)-1 

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1 
                r -= 1

        return True

        