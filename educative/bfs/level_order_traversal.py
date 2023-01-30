"""
Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  q = deque()
  q.append(root)
  while q:
    level_size = len(q)
    curr_level = []
    for _ in range(level_size):
      node = q.popleft()
      curr_level.append(node.val)
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    result.append(curr_level)
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
