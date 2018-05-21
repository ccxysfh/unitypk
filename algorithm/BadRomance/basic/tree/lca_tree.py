#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: lca_tree.py
@time: 2018/5/20 00:17
"""
class Node(object):
    
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)
    
class BinaryTree(object):
    
    def lca(self, root, node1, node2):
        if None in (root, node1, node2):
            return None
        if not self._node_in_tree(root, node1) or \
            self._node_in_tree(root, node2):
            return None
        return self._lca(root, node1, node2)

    def _node_in_tree(self, root, node):
        if root is None:
            return None
        if root is node:
            return True
        left = self._node_in_tree(root.left, node)
        right = self._node_in_tree(root.right, node)
        return left or right

    def _lca(self, root, node1, node2):
        if root is None:
            return False
        if root is node1 or root is node2:
            return root
        left_node = self._lca(root.left, node1, node2)
        right_node = self.lca(root.right, node1, node2)
        if left_node is not None and right_node is not None:
            return root
        return left_node if left_node else right_node
        
    

    

if __name__ == '__main__':
    pass