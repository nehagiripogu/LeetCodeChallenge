# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque([(root,0)])
        visited=set()
        res=[]
        ans=0
        while q:
            level=[]
            for i in range(len(q)):
                node,index=q.popleft()
                visited.add(node)
                level.append(index)
                if node.left:
                    q.append((node.left,2*index+1))
                
                if node.right:
                    q.append((node.right,2*index+2))
            ans=max(ans,level[-1]-level[0]+1)
                
            res.append(level)
        
        return ans