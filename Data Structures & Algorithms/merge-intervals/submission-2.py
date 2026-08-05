#Understand ->
# Scan through each array 
#   find the start ad end
# if start or end overlap with an arrray
# merge anc create another interval

#for no overlapping, just return unchanged array


#Plan ->
#create an empty list of results
# create 2 ptrs : if start[i] == start[j]
## then check which end is bigger 
### update the array with end[i] or end[j] 
# else just add non overlapping array to list

#BOH -> 
# create a dictionary?

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(end,lastEnd)
            else:
                output.append([start, end])
        return output


            
            
            
    