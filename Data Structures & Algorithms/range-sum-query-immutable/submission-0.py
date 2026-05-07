
class NumArray:
    def __init__(self, nums: List[int]):
        # 1. Initialize self.prefix with an extra 0 at the start 
        # to make range logic cleaner.
        self.prefix = [0] * (len(nums) + 1)

        
        # 2. Pre-calculate the prefix sums once
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # 3. Use the formula: Sum(left, right) = Prefix[right + 1] - Prefix[left]
        return self.prefix[right + 1] - self.prefix[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)