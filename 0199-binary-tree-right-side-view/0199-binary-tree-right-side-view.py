# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        q = collections.deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    q.append(node.right)
                    q.append(node.left)
                    level.append(node.val)
            if level:
                levels.append(level)
        right_nodes = []
        for level in levels:
            right_nodes.append(level[0])
        return right_nodes
