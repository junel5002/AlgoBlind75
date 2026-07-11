class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, n in enumerate(nums): #O(n)
            if n in seen and i - seen[n] <= k: #O(1)
                return True #O(1)
            seen[n] = i #O(1)
        return False #O(1)

#note: time complexity is calculated line by line; if something is indented,
# we multiply but if on the same line, we add
#NB: a look up in a hash map is always O(1) and return True or return False
# is also O(1); now to calcuate the time complexity = O(n) * [O(1)*O(1) + O(1) + O(1)]
# and this will give us O(n)