# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, currMax):
            if not node:
                return 0
            
            res = 1 if node.val >= currMax else 0
            res += dfs(node.left, max(currMax, node.val))
            res += dfs(node.right, max(currMax, node.val))
            return res
        res = dfs(root, float("-infinity"))
        return res

        def bfs(root):
            if not root:
                return 0
            q = deque([(root, float("-infinity"))])
            res = 0
            while q:
                node, maxValue = q.popleft()
                if node.val >= maxValue:
                    res += 1
                if not node.left:
                    q.append((node.left, max(maxValue, node.val))) 
                if not node.right:
                    q.append((node.right, max(maxValue, node.val))) 
            return res
        return bfs(root)

