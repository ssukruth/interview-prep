"""
Find start of linked list cycle
"""

from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()


"""
Use two pointers.
make the first one traverse N nodes where N is cycle len
Traverse both the pointers until they meet at a node, that's the start of the cycle.
"""

def find_cycle_start_node(head, cycle_len):
  p1, p2 = head, head
  while cycle_len > 0:
    p2 = p2.next
    cycle_len -= 1
  while p1 != p2:
    p1 = p1.next
    p2 = p2.next
  return p1

def find_cycle_len(slow):
  current = slow
  cycle_len = 0
  while True:
    current = current.next
    cycle_len += 1
    if current == slow:
      break
  return cycle_len

def find_cycle_start(head):
  fast, slow = head, head
  start = None
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      cycle_len = find_cycle_len(slow)
      start = find_cycle_start_node(head, cycle_len)
      break
  return start


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

