class Solution:
    def twoSum(self, nums, target):

        prevMap = {}    
        for index, num in enumerate(nums): #where i = the index, n = the number
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index
        return

"""note: the diff is used to now compare the keys/values in the hashmap which is the prevMap;
when the diff is one of the keys/values in the hashmap then you will just return
the index of that key in the hashmap and index of the num in the loop"""