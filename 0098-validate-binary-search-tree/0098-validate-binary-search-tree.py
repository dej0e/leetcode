# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

            def isValid(node, minval, maxval):
                if not (minval < node.val < maxval):
                    return False
                valid = True
                if node.left:
                    valid = valid and isValid(node.left, minval, node.val)
                if node.right:
                    valid = valid and isValid(node.right, node.val, maxval)
                return valid
            return isValid(root, float("-infinity"), float("infinity"))
