# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False  # Handle empty tree case
        
        path = []
        path.append(root.val)

        def btk(node, path):
            nonlocal targetSum
            if not node: return False  # Changed from 'root' to 'node'

            if not node.left and not node.right and sum(path) == targetSum:
                return True
            
            # Need to add to path before exploring children
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

        return btk(root, path)