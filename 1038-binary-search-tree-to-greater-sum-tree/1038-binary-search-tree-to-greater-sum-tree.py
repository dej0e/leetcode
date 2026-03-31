# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cursum = 0
        def dfs(node):
            if not node:
                return
            
            nonlocal cursum
            dfs(node.right)
            temp = node.val
            node.val += cursum
            cursum += temp

            dfs(node.left)
            return node
        dfs(root)
        return root