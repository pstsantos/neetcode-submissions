#Understand ->
#Check if any value of the list appears more than one time

#Plan -> 
#Create a set
#Loop through the array an ints to set
#If the current int (inside loop) is also in set
#THEN return false
#ELSE true

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasD = False
        seen = set()
        for i in nums:
          if i in seen:
             hasD = True
          seen.add(i)
        return hasD
        