from collections import deque
from typing import Optional, List

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        level = 0

        while queue:
            n = len(queue)
            new_level = deque()

            for _ in range(n):
                node = queue.popleft()
                if level % 2 == 0:
                    new_level.append(node.val)
                else:
                    new_level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(list(new_level))
            level += 1

        return res
