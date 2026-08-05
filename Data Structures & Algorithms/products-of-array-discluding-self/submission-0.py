#Understand -> 
# multiple all the elements of the array, but i for each element

#Plan-> for i in nums, add all elements to dictionary
# add to the product output count
# for i in dictionary, divide produt output count
#return 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        preFix = 1
        for i in range(len(nums)): #here confirm when to use what
            res[i] = preFix
            preFix *= nums[i]

        postFix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postFix
            postFix *= nums[i]
        
        return res
            

            
