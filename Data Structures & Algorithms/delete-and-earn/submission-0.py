class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        points = {}
        # Store each number and the total points we can get
        # from all copies of that number.

        for num in nums:
            # Go through every number in nums.

            points[num] = points.get(num, 0) + num
            # Add the number to its total.
            # Example: if num = 2 appears twice,
            # points[2] becomes 4.

        max_num = max(nums)
        # Find the largest number in nums.
        # We will check every value from 1 to max_num.

        prev2 = 0
        # Best score from two values back.

        prev1 = 0
        # Best score from the previous value.

        for value in range(1, max_num + 1):
            # Check each possible value one by one.

            take = prev2 + points.get(value, 0)
            # If we TAKE this value,
            # we cannot take the value right before it.
            # So we add this value's points to prev2.

            skip = prev1
            # If we SKIP this value,
            # keep the best score we already had.

            current = max(take, skip)
            # Pick whichever option gives more points:
            # take this value or skip it.

            prev2 = prev1
            # Move prev2 forward for the next round.

            prev1 = current
            # Save the best score up to this value.

        return prev1
        # Return the maximum points we can earn.