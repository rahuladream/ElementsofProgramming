"""
Continous subarray
"""


class Solution:
    def findMaxLength(self, nums):

        if len(nums) < 2:
            return 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        

        hash_value = {}

        res = 0

        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]

            if prefix == 0:
                res = i + 1
            
            elif prefix not in hash_value:
                hash_value[prefix] = i

            else:
                res = max(res, i - hash_value[prefix]) 
        return res       