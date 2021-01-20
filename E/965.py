# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        vals = []
        
        def dfs( node ):
            
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        
        return len(set(vals)) == 1
