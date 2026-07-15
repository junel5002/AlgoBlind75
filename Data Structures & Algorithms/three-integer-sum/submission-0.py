class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #for this problem we can basically take one number then we use two pointers to
        #get the other two numbers that will make everything == 0:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            # If the first number is greater than 0,
            # then all numbers after it are also greater than 0.
            # So we cannot make a sum of 0 anymore.
            if nums[i] > 0:
                break

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res