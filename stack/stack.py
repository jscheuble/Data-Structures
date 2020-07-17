"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   with a linked list, we only have access to the head and the tail directly. 
   We can still iterate over arrays, but we don't need that functionality with a stack. 
   All we need is to reference the head and the tail, and the next pointer from each node,
   making linked lists a more preferrable option.
"""
from singly_linked_list.singly_linked_list import LinkedList


# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = self.size + 1

#     def pop(self):
#         if self.size > 0:
#             self.size = self.size - 1
#             return self.storage.pop()
#         else:
#             return None


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.size + 1

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            return self.storage.remove_tail()
        else:
            return None
