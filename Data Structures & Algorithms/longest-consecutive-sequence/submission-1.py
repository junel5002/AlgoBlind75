class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 #keeps track of the current longest length

        for n in numSet:
            # check if n is the start of a sequence
            if (n - 1) not in numSet:
                length = 0

                while (n + length) in numSet:
                    length += 1

                longest = max(longest, length) #updates to the longest at the top

        return longest

"""
1. Put all numbers into a set.
2. Only start counting when the previous number does not exist.
3. Count upward until the sequence breaks.
4. Keep the largest length found.
"""