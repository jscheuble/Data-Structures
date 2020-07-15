"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        # check for empty list
        if self.head is None and self.tail is None:
            # set new node to head and tail
            self.head = new_node
            self.tail = new_node
        else:  # if list is not empty
            # set next to current head
            new_node.next = self.head
            # set new node to current head.prev
            self.head.prev = new_node
            # set new node to head
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        current = self.head
        # check if head has a next value
        if current.next is not None:
            # remove connection between current and next
            current.next.prev = None
            # set new head to current head's next value
            self.head = current.next
        else:  # if head.next is None
            # remove only node in the list
            self.head = None
            self.tail = None
        # decrement length
        self.length -= 1
        return current.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        # check for empty list
        if self.head is None:
            # set new node to head and tail
            self.head = new_node
            self.tail = new_node
        else:  # if list is not empty
            # set new node's previous to old tail
            new_node.prev = self.tail
            # set old tail's next to new node
            self.tail.next = new_node
            # set new node as new tail
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        tail = self.tail
        # only decrement length if it is greater than zero
        if self.length > 0:
            self.length -= 1
        # check if tail has prev value
        if tail.prev is not None:
            # remove connection to old tail
            tail.prev.next = None
            # declare new tail
            self.tail = tail.prev
        else:  # if length is 1
            # remove only node in the list
            self.head, self.tail = None, None
        return tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # remove node from list & store in variable
        new_head = self.delete(node)
        # add variable to head of the list
        self.add_to_head(new_head)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # remove from list & store in variable
        new_tail = self.delete(node)
        # add variabel to end of the list
        self.add_to_tail(new_tail)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        # do nothing if list is empty
        if self.length == 0:
            return

        # increment length
        self.length -= 1

        # list has one node
        if self.head is self.tail:
            self.head, self.tail = None, None
            return node.value

        # delete head
        elif node is self.head:
            self.head = self.head.next
            node.next, self.head.prev = None, None
            return node.value

        # delete tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.prev, self.tail.next = None, None
            return node.value

        # delete from middle
        else:
            prev, next_node = node.prev, node.next
            prev.next, next_node.prev = node.next, node.prev
            return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current = self.head
        max = 0

        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next

        return max
