#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: min_bst.py
@time: 2018/5/23 14:02
"""
"""
create a binary search tree with minist heigth from a sorted array
"""
from basic.tree.binary_search_tree import BinarySearchTree, BinaryTreeNode

class MinBst(BinarySearchTree):
    
    def __init__(self, ):
        super(MinBst, self).__init__()

    def min_bst(self, sorted_array):
        if sorted_array is None:
            return None
        return self._min_bst(sorted_array, 0, len(sorted_array) -1 )

    def _min_bst(self, array, start, end):
        if start > end:
            return
        mid = (end + start) // 2
        node = BinaryTreeNode(array[mid])
        node.left = self._min_bst(array, start, mid - 1)
        node.right = self._min_bst(array, mid + 1, end)
        return node

if __name__ == '__main__':
    pass