class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        #always assign L = 0 and R = len(nums) - 1 so that your code is simple
        L = 0
        R = len(nums) - 1

        while L <= R:  #always make sure it's <= and not <
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid - 1

        return -1