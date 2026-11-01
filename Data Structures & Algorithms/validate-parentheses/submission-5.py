'''
every ( ---> )
open bracket are closed in the correct order.


s = "(]"

s = "([{}])"

(
[
{

'''

class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []
        opentoClose = {
            ')':'(',
            ']':'[',
            '}':'{'
        }


        for char in s:

            if char in opentoClose:
                if stack and stack[-1] == opentoClose[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False