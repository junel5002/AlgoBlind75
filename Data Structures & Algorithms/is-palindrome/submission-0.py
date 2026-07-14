class Solution:
    def isPalindrome(self, s: str) -> bool:
        
# this is another way to solve it; less efficient
# we use a built in python function called .isalnum(), meaning if the char
# is alphanumeric then do blah blah blah

        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower() #so we just convert all chars into lowercase
        return newStr == newStr[::-1] #this returns true if they are the same otherwise false

