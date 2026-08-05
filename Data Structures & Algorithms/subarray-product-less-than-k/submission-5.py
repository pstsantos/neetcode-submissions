class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        L, total = 0,1
        res = 0

        for R in range(len(nums)):
            total *= nums[R]
            #deleted my edge case#
            while L <= R and total >= k :
                total /= nums[L]  
                L += 1
            res += (R - L + 1)   
        return res 
