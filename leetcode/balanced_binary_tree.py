"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node):
            if not node:
                return [True, 0]
            l = dfs(node.left)
            r = dfs(node.right)
            balanced = (l[0] and r[0]) and abs(l[1] - r[1]) <= 1
            return [balanced, 1 + max(l[1], r[1])]

        return dfs(root)[0]
