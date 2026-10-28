class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
              s[left], s[right] = s[right], s[left]
              left += 1 
              right -= 1

#NB: set left = 0, set right to equal to length of string - 1, while left less right, we swap the characters at left and right and move left forward by 1 and move right backward by one and finally stop when the pointers meet or cross.
        """
        Do not return anything, modify s in-place instead.
        """
        