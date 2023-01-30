class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)
            return max(helper(node.left, curr_max, curr_min),
                       helper(node.right, curr_max, curr_min))

        return helper(root, root.val, root.val)
