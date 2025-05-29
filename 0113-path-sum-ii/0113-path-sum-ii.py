# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, remaining, path):
            if node is None:
                return
            path.append(node.val)  # update path
            remaining -= node.val
            if node.left is None and node.right is None and remaining == 0:  # is_leaf
                paths.append(path[:])
            else:  # edges = [node.left, node.right]
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)
            path.pop()  # revert path

        paths = []
        dfs(root, targetSum, [])
        return paths
