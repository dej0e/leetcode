# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if tree1 is None and tree2 is None:
                return True
            if tree1 is None or tree2 is None:
                return False
            return (
                (tree1.val == tree2.val)
                and isSameTree(tree1.left, tree2.left)
                and isSameTree(tree1.right, tree2.right)
            )

        if not root:
            return False
        return (
            isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )
