import sys
import time       # to construct the second plot
import unittest
from typing import *
from dataclasses import dataclass
import math
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)

from bst import *

TREES_PER_RUN: int = 5000


# builds a random binary search tree with n random float values between 0 and 1
def random_tree(n: int) -> BinarySearchTree:
    def comes_before(a, b):
        return a < b
    bst = BinarySearchTree(comes_before=comes_before, bintree=None)
    for i in range(n):
        val = random.random()
        bst = insert(bst, val)
    return bst

# finds the height of a binary tree
def height(node: BinTree) -> int:
    if node is None:
        return 0
    left_h = height(node.left)
    right_h = height(node.right)
    if left_h > right_h:
        return 1 + left_h
    else:
        return 1 + right_h

# finds the average height from TREES_PER_RUN random trees with n nodes
def average_height(n: int) -> float:
    total = 0
    for i in range(TREES_PER_RUN):
        bst = random_tree(n)
        total = total + height(bst.bintree)
    return total / TREES_PER_RUN

# creates a graph showing average BST height vs number of nodes
def average_height_graph() -> None:
    n_max: int = 100
    n_values: List[float] = [float(v) for v in np.linspace(0, n_max, 50)]
    heights: List[float] = [average_height(int(x)) for x in n_values]

    x_numpy: np.ndarray = np.array(n_values)
    y_numpy: np.ndarray = np.array(heights)

    plt.plot(x_numpy, y_numpy, label="Average BST Height")
    plt.xlabel("N (number of nodes)")
    plt.ylabel("Average Height")
    plt.title("Average Height of Random BSTs")
    plt.grid(True)
    plt.legend()
    plt.show()


# creates a graph showing average insert time vs number of nodes
def average_insert_time_graph() -> None:
    n_max: int = 100
    n_values: List[int] = [int(v) for v in np.linspace(0, n_max, 50)]
    avg_times: List[float] = []
    def comes_before(a, b): return a < b

    for n in n_values:
        start = time.perf_counter()
        for i in range(TREES_PER_RUN):
            bst = BinarySearchTree(comes_before=comes_before, bintree=None)
            for j in range(n):
                bst = insert(bst, random.random())
            bst = insert(bst, random.random())  # insert one more into size-n tree
        end = time.perf_counter()
        avg_times.append((end - start) / TREES_PER_RUN)

    x = np.array(n_values, dtype=float)
    y = np.array(avg_times, dtype=float)
    plt.plot(x, y, label="Average Insert Time (seconds)")
    plt.xlabel("N (number of nodes)")
    plt.ylabel("Average Insert Time (s)")
    plt.title("Average Time to Insert into Random BST vs Tree Size")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == '__main__': # having trouble running both at same time, doing one at a time
    #average_height_graph()
    average_insert_time_graph()
