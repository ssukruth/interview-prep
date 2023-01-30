class Solution(object):
    def inorder(self, root, order):
        if not root:
            return
        self.inorder(root.left, order)
        order.append(root)
        self.inorder(root.right, order)

    def build(self, nodes):
        if not nodes:
            return
        mid = len(nodes)//2
        new_root = nodes[mid]
        new_root.left = self.build(nodes[:mid])
        new_root.right = self.build(nodes[mid+1:])
        return new_root

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        order = []
        # Get the inorder traversal
        self.inorder(root, order)
        # Build BST from inorder traversal
        return self.build(order)

