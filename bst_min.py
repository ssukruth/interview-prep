# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = None
        self.count = 1
        def dfs(root):
            if not root: return
            if self.res: return
            dfs(root.left)
            if self.res is None and self.count == k:
                self.res = root.val
                return
            self.count += 1
            dfs(root.right)

        dfs(root)
        return self.res
