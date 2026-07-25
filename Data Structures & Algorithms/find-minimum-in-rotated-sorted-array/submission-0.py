class Solution:
    def findMin(self, nums: List[int]) -> int:

        #We will use the approach such that when nums[L] == nums[R] then that's the minimum

        L = 0
        R = len(nums) - 1

        while L < R:
            mid = (L + R) // 2 #NB: This rounds the decimal down to the nearest whole number

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid  #NB: We equate the right pointer to mid because the mid in that case can be the minimum

        return nums[L]