#Understand -> 
#find a subarray of numbers with the largest sum

# it needs to be a continguous non-empty sequence
#EDGE CASE : if array has only one element return the i

#create a max subA and set it to 0
#create an array to store values
#loop through each i
#1ST // check if i is bigger than current sum
# if yes -> then add it to list
# if no -> move on to the next and reset sum 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentStreak = 0
        strongestStreak = nums[0]

        for i in nums: 
            if currentStreak < 0: 
                currentStreak = 0
            currentStreak += i
            strongestStreak = max(strongestStreak, currentStreak)   
        return strongestStreak




