class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] # answer 
        subset = [] #subset

        def dfs(i, current_target): #dfs/ bkt
            if current_target == 0:
                res.append(subset.copy()) # append a new subset
                return
            
            if i >= len(nums) or current_target < 0:
                return

            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i, current_target - nums[i]) # same index because we can reuse number

            # Decision to NOT include nums[i]
            subset.pop()
            dfs(i + 1, current_target)
            
        dfs(0, target) #start by first index 
        return res # return answer