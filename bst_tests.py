import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *

X_cord: TypeAlias = float
Y_cord: TypeAlias = float
@dataclass(frozen=True)
class Point2:
    x: X_cord
    y: Y_cord

def int_comes_before(a, b):
    return a < b

def str_comes_before(a, b):
    return a < b

def point_comes_before(a, b):
    # order by Euclidean distance from (0,0)
    return (a.x * a.x + a.y * a.y) < (b.x * b.x + b.y * b.y)

class BSTTests(unittest.TestCase):
    def test_integers(self):
        bst = BinarySearchTree(comes_before=int_comes_before, bintree=None)
        self.assertTrue(is_empty(bst))
        bst = insert(bst, 10)
        bst = insert(bst, 5)
        bst = insert(bst, 15)
        self.assertFalse(is_empty(bst))
        self.assertTrue(lookup(bst, 10))
        self.assertFalse(lookup(bst, 7))
        bst = delete(bst, 10)
        self.assertFalse(lookup(bst, 10))

    def test_strings(self):
        bst = BinarySearchTree(comes_before=str_comes_before, bintree=None)
        bst = insert(bst, "delta")
        bst = insert(bst, "alpha")
        bst = insert(bst, "charlie")
        self.assertTrue(lookup(bst, "alpha"))
        self.assertFalse(lookup(bst, "bravo"))
        bst = delete(bst, "alpha")
        self.assertFalse(lookup(bst, "alpha"))

    def test_points_by_distance(self):
        bst = BinarySearchTree(comes_before=point_comes_before, bintree=None)
        point0 = Point2(0, 0)
        point1 = Point2(3, 4)
        point1_eq = Point2(-3, 4)
        point2 = Point2(1, 1)
        bst = insert(bst, point1)
        bst = insert(bst, point0)
        bst = insert(bst, point2)
        self.assertTrue(lookup(bst, point1))
        self.assertTrue(lookup(bst, point1_eq))
        self.assertTrue(lookup(bst, point0))
        bst = delete(bst, point1)
        self.assertTrue(lookup(bst, point1_eq))
        bst = delete(bst, point1_eq)
        self.assertFalse(lookup(bst, point1))
        self.assertFalse(lookup(bst, point1_eq))


if (__name__ == '__main__'):
 unittest.main() 
