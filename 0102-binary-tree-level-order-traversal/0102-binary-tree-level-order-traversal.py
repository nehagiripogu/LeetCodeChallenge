# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def dfs(res,root,depth):
            if root==None:
                return
            if len(res)==depth:
                res.append([])
            res[depth].append(root.val)
            dfs(res,root.left,depth+1)
            dfs(res,root.right,depth+1)
        dfs(res,root,0)
        return res
