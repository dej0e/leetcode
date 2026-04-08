# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        indices = {n: i for i, n in enumerate(inorder)}
        self.preIdx = 0
        root_val = preorder[0]
        root = TreeNode(root_val)
        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.preIdx]
            self.preIdx += 1
            mid = indices[root_val]
            root = TreeNode(root_val)
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(preorder) - 1)