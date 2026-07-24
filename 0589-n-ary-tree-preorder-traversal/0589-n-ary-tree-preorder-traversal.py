# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        def dfs(root,res):
            if root==None:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child,res)
        
        dfs(root,res)
        return res