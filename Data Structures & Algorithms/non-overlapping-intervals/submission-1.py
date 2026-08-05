#Understand -> Remove intervals that overlap

#Plan -> 
# Sort intervals 
# create a temp array
# for loop starting on second index
## cutout will be the non-overlapping
### add them to list
# do length of inteval array - temp array
# return difference 


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        lastEnd = intervals[0][1]
        remove = 0

        for start, end in intervals[1:]:
            if start >= lastEnd:
                lastEnd = end
            else: 
                remove += 1
                lastEnd = min(end,lastEnd)

        return remove 



        