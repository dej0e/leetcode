# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = [float("infinity")]
        def dfs(node):
            nonlocal count
            if not node:
                return
            
            dfs(node.left)
            count -= 1
            if count == 0:
                res[0] = node.val
                return
            dfs(node.right)

        dfs(root) 
        return res[0]