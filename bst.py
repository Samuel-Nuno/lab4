import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 
import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6) 

BinTree: TypeAlias = Union[None, 'Node']
Value : TypeAlias = Any

@dataclass(frozen=True)
class Node:
    value: Value
    left: BinTree
    right: BinTree



@dataclass(frozen=True)
class BinarySearchTree:
    #value : comes_before
    bintree: BinTree

# intake BinarySearchTree and rerurns True (tree is empty) or False (otherwise)
def is_empty( bst : BinarySearchTree) -> bool:
    pass

# adds input value to BST using comes_before and determines which path to take (left or right) at each node
def insert(bst: BinarySearchTree, val: Value) -> BinarySearchTree:
    pass

# intakes BinarySearchTree and a value, returns True (value is stored) or False (otherwise)
def lookup (bst : BinarySearchTree , val : Value) -> bool:
    " uses comes_before, not less than. If neither value 'comes before' the other, then they will be considered equal"
    pass 
    
# removes the input value and preserves the BinarySearchTree. In the case of duplicate, only removes one of the values
def delete(bst: BinarySearchTree, val: Value) -> BinarySearchTree:
    pass
 
 

