#find num of paths which have the target sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        from collections import defaultdict
        self.result = 0

        def helper(node, prefix_sum, cache):
            if not node:
                return

            prefix_sum += node.val
            complement = prefix_sum - targetSum
            self.result += cache[complement]
            cache[prefix_sum] += 1
            helper(node.left, prefix_sum, cache)
            helper(node.right, prefix_sum, cache)
            cache[prefix_sum] -= 1

        cache = defaultdict(int)
        cache[0] = 1
        helper(root, 0, cache)
        return self.result
