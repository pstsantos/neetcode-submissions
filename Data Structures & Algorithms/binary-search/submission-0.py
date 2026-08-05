#Understand - Find the target within a list and return the index
#if target not found return -1
#### sorted

#Plan -> 
#create l, r and mid
# while loop 
## if target < mid UPDATE r
## if target > mid UPDATE l
### if target == mid RETURN i
# else return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        