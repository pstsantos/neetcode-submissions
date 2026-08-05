#Understand -> Find two numbers that add up to the target, 
# return an array [0,1] with the smallest value first
#constraint they cannot be the same and there will alaways be a value

#Plan ->
#create a dictionary/hashmap
#create an answer array
#add all the values in there
#for loop it 
## if difference = 0 return it as an answer
## answer = min(value, difference)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
            


   
        


        
                



            