class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        res = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        
        for i in range(1, len(nums)):
            n = nums[i]
            
            # If we encounter a negative number, max and min swap roles
            if n < 0:
                curr_max, curr_min = curr_min, curr_max
            
            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)
            
            res = max(res, curr_max)
            
        return res