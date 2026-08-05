#U -> remove ANY occurence of val (in place), return remainder k
#P -> #start ptr l = 0 
      # for loop starting at 1, looping through r
      # if l is equal val THEN make that have the same value as R
      # move l foward
      #return the lenght of the array

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k