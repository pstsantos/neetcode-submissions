# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque()

        if root:
            queue.append(root)

        while len(queue):
            leaf = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    leaf.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if leaf: # why?
               res.append(leaf)
        return res