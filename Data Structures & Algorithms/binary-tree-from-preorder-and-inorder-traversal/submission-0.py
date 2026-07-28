# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderObj = {}
        for i, val in enumerate(inorder):
            inorderObj[val] = i
        preOrderIndex = 0
        def dfs(left,right):
            nonlocal preOrderIndex
            if left > right:
                return None
            rootvalue = preorder[preOrderIndex]
            preOrderIndex += 1
            root = TreeNode(rootvalue)
            mid = inorderObj[rootvalue]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root 
        return dfs(0,len(inorder)-1)