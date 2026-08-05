#Understand -> scan through each element of an array 
# and return TRUE IF there are duplicates, 
# ELSE FALSEN if there are negatives

#Plan -> create a set and add elements of the array
# compare if i element is same in array & set
# if not true return FALSE
# else TRUE


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        hasD = True

        for i in nums:
            myset.add(i)

        if len(nums) == len(myset):
            hasD = False
        
        return hasD
        