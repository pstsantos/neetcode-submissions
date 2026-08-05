#U -> resize an array, first fill it with nums, then fill it again with the same numbers
#P -> 

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * 2 * len(nums)
        half = round(len(ans)/2)

        # Copy elements to new array
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + half]  = nums[i] #find a way to pluf them at the same time mathematically

        return ans