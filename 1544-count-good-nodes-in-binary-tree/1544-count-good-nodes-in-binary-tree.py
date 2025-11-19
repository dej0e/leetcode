# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_so_far: int) -> int:
            if not node:
                return 0
            total = 0
            if node.val >= max_so_far:
                total+=1
            max_so_far = max(node.val, max_so_far)
            total += dfs(node.left, max_so_far)
            total += dfs(node.right, max_so_far)
            return total
        return dfs(root, float("-infinity"))