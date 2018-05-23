#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: validate_bst.py
@time: 2018/5/23 14:26
"""
"""
Determine if a tree is a valid binary search tree
"""
import sys
from basic.tree.binary_search_tree import BinarySearchTree

class ValidateBst(BinarySearchTree):

    def validate_bst(self):
        if self.root is None:
            raise TypeError("root can't be None")
        return self._validate(self.root)

    def _validate(self, node, minimum=-sys.maxsize, maximum=sys.maxsize):
        if node is None:
            return True
        if node.data <= minimum or node.data > maximum:
            return False
        if not self._validate(node.left, minimum, node.data):
            return False
        if not self._validate(node.right, node.data, maximum):
            return False
        return True


if __name__ == '__main__':
    pass