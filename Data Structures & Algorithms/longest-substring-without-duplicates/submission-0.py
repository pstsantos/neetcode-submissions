
#Understand -> 
# Find the longest chain of unique elements 

#Plan -> open a set called seen and add 
#it will involve resetting atsp
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniques = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in uniques:
                uniques.remove(s[l])
                l += 1
            uniques.add(s[r])
            res = max(res, len(uniques))
        return res