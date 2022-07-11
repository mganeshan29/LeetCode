# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        
        q, res, ele = deque([root]), [], 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                ele = node.val # this will store particular val at a single level
                q.append(node.left) if node.left else ...
                q.append(node.right) if node.right else ...
            res.append(ele) # this will only have the last value of the level after the end of the for loop.
        return res