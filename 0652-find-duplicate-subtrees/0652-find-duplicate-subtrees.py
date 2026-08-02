# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        freq = {}
        res = []

        def dfs(node):
            if not node:
                return "#"

            left = dfs(node.left)
            right = dfs(node.right)

            subtree = str(node.val) + "," + left + "," + right

            freq[subtree] = freq.get(subtree, 0) + 1

            if freq[subtree] == 2:
                res.append(node)

            return subtree

        dfs(root)

        return res