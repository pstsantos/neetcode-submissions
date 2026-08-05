#understand: FIND HOW MAY DIFFERENT WAYS ONE CAN ACHIEVE N NUMBER OF STEPS
#plan: 
## BASE CASE -> if sum is 0
## ELSE -> increment count
## call function with (N-1) and (N-2)
# return call


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1,1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp       
    
        return one 


        