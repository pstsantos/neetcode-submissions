# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Understand -> Find a path that evaluates to the target sum. 
# Return T/F if one was found

#Plan -> 
# create a path array
# estabilish base case 1 - if no node, False
# estabilish base case 2 - if a leaf was found, True and sum of array == target
# recurse on both ways L and R
# pop values and try another route
#return False

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        path = []
        path.append(root.val)

        def btk(node, path):
            nonlocal targetSum
            if not node: return False

            if not node.left and not node.right and sum(path) == targetSum:
                return True
            
            if node.left:
                path.append(node.left.val)
                if btk(node.left, path):
                    return True
                path.pop()
            
            if node.right:
                path.append(node.right.val)
                if btk(node.right, path):
                    return True
                path.pop()
                
            return False
        return btk(root,path)

        

        




        

        
