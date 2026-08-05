# Understand -> 
# find the shortest subarray where the sum is = or > the target

#Plan ->
# Mix of bin search + sliding window
# Sort the array

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        ans = float("inf")

        if sum(nums) < target:
            return 0

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(r - l + 1, ans)
                total -= nums[l]
                l += 1 
        return ans 
