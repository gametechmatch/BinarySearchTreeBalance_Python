#################################################################
# BinarySearchTreeProgramT.py
#################################################################
# Author: gametechmatch
# Course: Data Structures
# CH8 - Binary Trees
# HW5 - WK5
# Programming Project 8.1
#################################################################
# Code in fillTree.() and evaluateTree.() functions have code from:
# Source Title: BinarySearchTreeClient.py
# Source Type: Book
# Source Title: Data Structures & Algorithms in Python
# Source Authors: John Canning, Alan Broder, & Robert Lafore
#################################################################
# Automated tests of the BinarySearchTree class
#################################################################
from BinarySearchTreeT import *
import sys

def main():
   print("############################################################")
   print(" EVALUATE BY THRESHOLD OF 0")
   print("############################################################")
   # Create an empty binary search tree
   treeOne = BinarySearchTree()
   # Create a list of values to insert into the binary search tree
   values = [7, 6, 5, 4, 3, 2, 1, 8, 12, 10, 9, 11, 14, 13, 15]
   # Fill in the values
   fillTree(treeOne, values)
   # Evaluate tree
   evaluateTree(treeOne)
   # Evaluate the Balance of the tree
   evaluateBalance(treeOne, 0)

   # Create an empty binary search tree
   treeTwo = BinarySearchTree()
   # Create a list of values to insert into the binary search tree
   values = [8, 4, 5, 6, 7, 3, 2, 1, 12, 10, 9, 11, 14, 13, 15]
   # Fill in the values
   fillTree(treeTwo, values)
   # Evaluate tree
   evaluateTree(treeTwo)
   # Evaluate the Balance of the tree
   evaluateBalance(treeTwo, 0)

   # Create an empty binary search tree
   treeThree = BinarySearchTree()
   # Create a list of values to insert into the binary search tree
   values = [8, 4, 2, 3, 1, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
   # Fill in the values
   fillTree(treeThree, values)
   # Evaluate tree
   evaluateTree(treeThree)
   # Evaluate the Balance of the tree
   evaluateBalance(treeThree, 0)

   # Create an empty binary search tree
   treeFour = BinarySearchTree()
   # Create a list of values to insert into the binary search tree
   values = [8, 4, 2, 3, 1, 6, 5, 7, 12, 10, 9, 11, 14, 13, 8.5]
   # Fill in the values
   fillTree(treeFour, values)
   # Evaluate tree
   evaluateTree(treeFour)
   # Evaluate the Balance of the tree
   evaluateBalance(treeThree, 0)

   # Evaluate additional thresholds
   print("\n############################################################")
   print(" EVALUATE BY THRESHOLD OF 1")
   print("############################################################")
   print("First Tree")
   evaluateBalance(treeOne, 1)
   print("Second Tree")
   evaluateBalance(treeTwo, 1)
   print("Third Tree")
   evaluateBalance(treeThree, 1)
   print("Fourth Tree")
   evaluateBalance(treeThree, 1)
   print("\n############################################################")
   print(" EVALUATE BY THRESHOLD OF 2")
   print("############################################################")
   print("First Tree")
   evaluateBalance(treeOne, 2)
   print("Second Tree")
   evaluateBalance(treeTwo, 2)
   print("Third Tree")
   evaluateBalance(treeThree, 2)
   print("Fourth Tree")
   evaluateBalance(treeThree, 2)

# This function inserts the values into the empty binary search tree.
# Print true for each insertion if value inserted. Print false if not
# (duplicate values)
def fillTree(binarySearchTree, values):
   if len(sys.argv) > 1:
      values = [int(a) for a in sys.argv[1:]]

   key = 0
   for value in values:
      print('Inserting value', value, 'in tree returns',
            binarySearchTree.insert(key, value))
      key += 1

   print("*****Binary Search Tree Fill Complete*****\n")

# This function prints information about a binary search tree
#################################################################
def evaluateTree(binarySearchTree):
   # Evaluate the binary search tree
   print('Created a binary search tree with', binarySearchTree.totalNodes(), 'nodes across',
         binarySearchTree.levels(), 'levels')
   binarySearchTree.print()
   root_key, root_value = binarySearchTree.root()
   print('The tree root node has key:', root_key, 'and value:', root_value)

   print("*****Binary Search Tree Evaluation Complete*****\n")

# This function prints information on how well balanced a binary search
# tree is
def evaluateBalance(binarySearchTree, by=1):
   # Find which nodes are unbalanced by their nodes and nodes
   # that are unbalanced by their levels
   binarySearchTree.unbalancedNodes(by)

   # Find the difference in the binary search tree's roots'
   # nodes and levels
   differenceInRightAndLeftNodes = binarySearchTree.nodeBalance()
   differenceInRightAndLeftLevels = binarySearchTree.levelBalance()

   # print the results
   print("___________________________________________________")
   print("Binary Search Tree's Root's Difference in Nodes: ")
   print({differenceInRightAndLeftNodes})
   print("___________________________________________________")
   print("Binary Search Tree's Root's Difference in Levels: ")
   print({differenceInRightAndLeftLevels})
   print("___________________________________________________")

   print("*****Binary Search Tree Balance Evaluation Complete*****\n")

# execute main function
if __name__ == '__main__':
	main()
