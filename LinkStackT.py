#################################################################
# LinkStackT.py
#################################################################
# Source Title: LinkStack.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Set up a Stack using a linked list data structure.
# The binary search tree file imports this file.
#################################################################
from LinkedListT import *
# Stack class that is a child class of the LinkedList class
#################################################################
class Stack(LinkedList):               # Define stack by renaming
   push = LinkedList.insert            # Push is done by insert
   pop = LinkedList.deleteFirst        # Pop is done by deleteFirst
   peek = LinkedList.first             # Peek is done by first
