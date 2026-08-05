# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortH(pairs, 0, len(pairs)-1)
            
    def mergeSortH(self, pairs: List[Pair], s : int , e : int) -> List[Pair]:
        if e - s + 1 <= 1: 
            return pairs
        
        #middle
        m = (s + e) // 2

        self.mergeSortH(pairs, s, m) #sort left side
        self.mergeSortH(pairs, m+1, e) #sort right side

        self.merge(pairs, s, m, e)

        return pairs

        #helper method to sort in-place
    def merge(self, pairs: List[pairs], s: int, m: int, e: int) -> None:
        l = pairs[s : m + 1]
        r = pairs[m + 1 : e + 1]

        i = 0 # half 1
        j = 0 # half 2
        k = s #actual array 

        while i < len(l) and j < len(r):
            if l[i].key <= r[j].key:
                pairs[k]= l[i]
                i += 1
            else:
                pairs[k] = r[j]
                j += 1
            k += 1

            # while the remainingn list still have item(s)
        while i < len(l):  
            pairs[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            pairs[k] = r[j]
            j += 1
            k += 1
            


        

