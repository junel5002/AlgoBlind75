class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        stack = [] #this is to store only numbers

        operators = {"+": lambda x,y: x+y,
                    "-": lambda x,y: x-y,
                     "/": lambda x,y: int(x/y),
                     "*": lambda x,y: x*y }

        for tk in tokens:
            if not tk in operators:
                stack.append(int(tk))
            else:
                right = stack.pop()
                left = stack.pop()
                val = operators[tk](left, right)
                stack.append(val)
            print(stack)
        return stack.pop()

#use this solution to make you stand out

#in the olden days this is how operation on a set of numbers is done
# IN method: so for this one, the operation is in between the operands(numbers). for eg
# IN method: 2 + 3

# POST method: the operation comes after the numbers(operands). eg: 2 5 +

# PRE method: the operation comes before the operands: eg. / 2 3

#NB: they all mean the same thing and produce the same result, but for the question 
# above, they are using the POST method