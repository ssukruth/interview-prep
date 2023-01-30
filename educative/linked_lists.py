# ### Typical Node representation in python ###
#  class Node:
#      def __init__(self, data):
#          self.data = data  # Data field
#          self.next_element = None  # Pointer to next node
#
# ### Typical Linked List representation in python ###
#  class LinkedList:
#      def __init__(self):
#          self.head_node = None  # Pointer to first node



class LinkedList:
    def __init__(self):
        self.head_node = None

    # Insertion at Head: O(1)
    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        self.head_node = temp_node  # Make the head point to the new node
        return self.head_node  # return the new list

    # Check if Head is empty: O(1)
    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False

    # Traverse list and insert: O(n)
    def insert_at_tail(lst, value):
        # Creating a new node
        new_node = Node(value)
        # Check if the list is empty, if it is simply point head to new node
        if lst.get_head() is None:
            lst.head_node = new_node
            return
        # if list not empty, traverse the list to the last node
        temp = lst.get_head()
        while temp.next_element:
            temp = temp.next_element
        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    # Traverse list and search: O(n)
    def search(lst, value):
        # Start from first element
        current_node = lst.get_head()
        # Traverse the list till you reach end
        while current_node:
            if current_node.data == value:
                return True  # value found
            current_node = current_node.next_element
        return False  # value not found

    # Traverse list and delete: O(n)
    def delete(lst, value):
        deleted = False
        if lst.is_empty():  # Check if list is empty -> Return False
            print("List is Empty")
            return deleted
        current_node = lst.get_head()  # Get current node
        previous_node = None  # Get previous node
        if current_node.data == value:
            lst.delete_at_head()  # Use the previous function
            deleted = True
            return deleted
        # Traversing/Searching for Node to Delete
        while current_node is not None:
            # Node to delete is found
            if value == current_node.data:
                # previous node now points to next node
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element
        if deleted == False:
            print(str(value) + " is not in list!")
        else:
            print(str(value) + " deleted!")
        return deleted

    # Traverse list and count: O(n)
    def length(lst):
        # start from the first element
        curr = lst.get_head()
        length = 0
        # Traverse the list and count the number of nodes
        while curr:
            length += 1
            curr = curr.next_element
        return length

    # Reverse in place: O(n)
    def reverse(lst):
      # To reverse linked, we need to keep track of three things
      previous = None # Maintain track of the previous node
      current = lst.get_head() # The current node
      next = None # The next node in the list
      #Reversal
      while current:
        next = current.next_element
        current.next_element = previous
        previous = current
        current = next
        #Set the last element as the new head node
        lst.head_node = previous
      return lst

    # Floyd's Cycle Finding Algorithm: O(n)
    def detect_loop(lst):
        # Keep two iterators
        onestep = lst.get_head()
        twostep = lst.get_head()
        while onestep and twostep and twostep.next_element:
            onestep = onestep.next_element  # Moves one node at a time
            twostep = twostep.next_element.next_element  # Skips a node
            if onestep == twostep:  # Loop exists
                return True
        return False

    # Find mid using 2 pointers: O(n)
    def find_mid(lst):
      if lst.is_empty():
        return -1
      current_node = lst.get_head()
      if current_node.next_element == None:
    		#Only 1 element exist in array so return its value.
        return current_node.data
      mid_node = current_node
      current_node = current_node.next_element.next_element
      #Move mid_node (Slower) one step at a time
      #Move current_node (Faster) two steps at a time
      #When current_node reaches at end, mid_node will be at the middle of List
      while current_node:
        mid_node = mid_node.next_element
        current_node = current_node.next_element
        if current_node:
          current_node = current_node.next_element
      if mid_node:
        return mid_node.data
      return -1

    # Traverse and remove duplicates in place : O(n)
    def remove_duplicates(lst):
        visited = {}
        prev = None
        curr = lst.get_head()
        if curr is None or curr.next_element is None:
            return lst
        while curr:
            if curr.data in visited:
                prev.next_element = curr.next_element
                curr.next_element = None
                curr = prev.next_element
            else:
                visited[curr.data] = True
                prev = curr
                curr = curr.next_element
        return lst

    # Find nth element: O(n)
    def find_nth(lst, n):
        l = lst.length()
        n = l - n + 1
        c = lst.get_head()
        while c:
            n -= 1
            if n == 0:
                return c.data
            c = c.next_element
        return -1
