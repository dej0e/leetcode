# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_node) -> int:
            if not node:
                return 0
            good_node_count = 0
            max_node = max(max_node, node.val)
            good_node_count += dfs(node.left, max_node)
            good_node_count += dfs(node.right, max_node)
            if node.val >= max_node:
                good_node_count += 1
            return good_node_count

        return dfs(root, -inf)
