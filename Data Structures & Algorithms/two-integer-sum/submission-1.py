#Understand -> 
# scan (loop) through the elements of nums 
# find two indexes that summed up equal target

#Plan ->
# create a dictionary
# create a variable called dif
# for each i -> check if dif = target - i -> is in the dictionary
# if not move on
# else return index *maybe using enumerate

#Implement ->
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsD = {}  # dictionary to store number:index pairs

        for i, n in enumerate(nums):
            difference = target - n

            if difference in numsD:
                return [numsD[difference], i]

            numsD[n] = i
    
            
        