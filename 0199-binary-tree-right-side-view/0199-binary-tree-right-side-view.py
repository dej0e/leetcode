# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        if not root:
            return res
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if not node:
                    continue
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
                if i == 0:
                    res.append(node.val)
        return res