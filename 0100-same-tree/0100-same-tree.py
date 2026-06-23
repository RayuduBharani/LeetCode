from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def Tree(root1 , root2) :
            if (root1 is None or root2 is None) :
                return root1 == root2
            if (root1.val != root2.val) :
                return False
            left = Tree(root1.left , root2.left)
            right = Tree(root1.right , root2.right)

            return left and right
        return Tree(p , q)