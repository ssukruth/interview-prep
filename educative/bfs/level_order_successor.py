"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  q = deque()
  q.append(root)
  found = False

  while q:
    level_size = len(q)
    for _ in range(level_size):
      node = q.popleft()
      if found:
        return node
      if node.val == key:
        found = True
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
  return None


def main():
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);

  result = find_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)

  result = find_successor(root, 9)
  if result:
    print(result.val)

  result = find_successor(root, 12)
  if result:
    print(result.val)


main()

