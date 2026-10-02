class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        unique = set()
        hasDupe = False

        for i in nums:
            if i not in unique :
                unique.add(i)
            else :
                hasDupe = True
            
                
        return hasDupe
        
        