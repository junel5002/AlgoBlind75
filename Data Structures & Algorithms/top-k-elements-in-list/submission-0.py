class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Sort by frequency
        sorted_nums = sorted(count, key=count.get, reverse=True)

        # Return first k elements
        return sorted_nums[:k]