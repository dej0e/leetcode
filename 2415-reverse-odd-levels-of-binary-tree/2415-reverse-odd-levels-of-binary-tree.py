# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        depth = 0
        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node)
            if depth % 2 == 1: #odd
                l = 0
                r = len(level) - 1
                while l <= r:
                    tempval = level[l].val
                    level[l].val = level[r].val
                    level[r].val = tempval
                    r -= 1
                    l += 1
            depth += 1

        return root
