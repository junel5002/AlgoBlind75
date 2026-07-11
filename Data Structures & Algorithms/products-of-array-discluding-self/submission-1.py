class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        postfix = [0] * n

        prefix[0] = postfix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
        for i in range(n):
            res[i] = prefix[i] * postfix[i]
        return res



"""
The key insight to remember whenever you see this problem, 
don't think: How do I multiply everything except this number?"
Instead think: I can get everything except this 
number by multiplying everything on its left and everything on its right
"""
