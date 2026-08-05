#(U)nderstand -> create a dictionary 
# to store the quantity of unique characters and 
# compare if its the same for the two strings 
# -> if yes, true/ else, false

#(P)lan -> create a HashMap/dictionary for both strings
# split the string
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
            return False

      return sorted(s) == sorted(t)


      