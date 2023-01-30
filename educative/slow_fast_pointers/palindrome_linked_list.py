"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have
O
(
N
)
O(N)
 time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list(head):
  fast, slow = head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
  mid = reverse(slow)
  mid_copy = mid
  while head and mid:
    if head.value != mid.value:
      return False
    head = head.next
    mid = mid.next
  reverse(mid_copy)
  if head is None or mid is None:
    return True
  return False


def reverse(head):
  prev = None
  while head:
    tmp = head.next
    head.next = prev
    prev = head
    head = tmp
  return prev



def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()



"""
Reverse LL:
    prev = None
    while head:
        tmp = head.next # need this to incremenet head
        #connect curr head to prev
        head.next = prev
        # set curr head to prev
        prev = head
        head = tmp

Palindrome LL:
    - find mid of LL
    - reverse from mid of LL
    - traverse from head & mid and check if values are the same.
    - reverse from mid just to reset the list to original form

"""
