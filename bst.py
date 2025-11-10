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
    comes_before: Callable[[Any, Any], bool]
    bintree: BinTree

# intake BinarySearchTree and returns True (tree is empty) or False (otherwise)
def is_empty( bst : BinarySearchTree) -> bool:
    if bst.bintree is None:
        return True
    else:
        return False

# adds input value to BST using comes_before and determines which path to take (left or right) at each node
def insert(bst: BinarySearchTree, val: Value) -> BinarySearchTree:
    def insert_node(comesbefore: Callable[[Any, Any], bool], node: BinTree, val2: Any) -> BinTree:
        if node is None:
            return Node(val2, None, None)
        if comesbefore(val2, node.value):  
            return Node(node.value, insert_node(comesbefore, node.left, val2), node.right)
        else:                  
            return Node(node.value, node.left, insert_node(comesbefore, node.right, val2))
    new_root = insert_node(bst.comes_before, bst.bintree, val)
    return BinarySearchTree(bst.comes_before, new_root)

# intakes BinarySearchTree and a value, returns True (value is stored) or False (otherwise)
def lookup (bst: BinarySearchTree , val: Value) -> bool:
    def lookup_node(comesbefore: Callable[[Any, Any], bool], node: BinTree, val2: Any) -> bool:
        if node is None:
            return False
        if (not comesbefore(val2, node.value)) and (not comesbefore(node.value, val2)):
            return True
        elif comesbefore(val2, node.value):
            return lookup_node(comesbefore, node.left, val2)
        else:
            return lookup_node(comesbefore, node.right, val2)
    return lookup_node(bst.comes_before, bst.bintree, val) 
    
# removes the input value and preserves the BinarySearchTree. In the case of duplicate, only removes one of the values
def delete(bst: BinarySearchTree, val: Value) -> BinarySearchTree:
    def delete_node(comesbefore: Callable[[Any, Any], bool], node: BinTree, val2: Any, extract_min: bool):
        if node is None and extract_min == False:
            return None
        elif node is None and extract_min == True:
            return (None, None)
        if extract_min == True:
            if node.left is None:
                return (node.right, node.value)
            new_left, min_val = delete_node(comesbefore, node.left, val2, True)
            return (Node(node.value, new_left, node.right), min_val)

        equal = (not comesbefore(val2, node.value)) and (not comesbefore(node.value, val2))

        if equal == True: 
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            new_right, succ_val = delete_node(comesbefore, node.right, val2, True)  
            return Node(succ_val, node.left, new_right)

        if comesbefore(val2, node.value):
            return Node(node.value, delete_node(comesbefore, node.left, val2, False), node.right)
        else:
            return Node(node.value, node.left, delete_node(comesbefore, node.right, val2, False))

    new_root = delete_node(bst.comes_before, bst.bintree, val, False)
    return BinarySearchTree(bst.comes_before, new_root)
 
 

