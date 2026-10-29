'''
all non-alphanumreric characters
case insensitive.

left, right = 0, len(s)

while l<=r:
    if not isalnum(s[l]):
        r -= 1
    else if not isalnum(s[r]):
        l += 1
    
    if s[l].lower() != s[r].lower():
        return False
    else:
        l += 1
        r -=
    
    return True

    e


Was it a car or a cat I saw?
^                         ^
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1


        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else: 
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1
            
        return True
