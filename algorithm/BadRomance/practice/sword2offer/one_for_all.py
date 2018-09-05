#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all.py
@time: 2018/9/5 09:57
"""
from basic.tree.binary_search_tree import BinaryTreeNode, Traversal
from basic.utils.results import Results

"""
题6 重建二叉树
根据前序遍历和中序遍历重建二叉树
"""


class ReconstructBinaryTree(object):

    def __init__(self, ):
        pass

    def construct(self, preorder: list, inorder: list):
        if not preorder or not inorder or len(preorder) != len(inorder):
            print('valid input')
            return

        root_index = inorder.index(preorder[0])
        root = BinaryTreeNode(preorder[0])
        root.left = self.construct(preorder[1: root_index+1], inorder[:root_index])
        root.right = self.construct(preorder[root_index+1:], inorder[root_index+1:])

        return root


def test_reconstruct_bt():
    rbt = ReconstructBinaryTree()
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    bt = rbt.construct(preorder, inorder)
    traversal = Traversal()
    results = Results()
    traversal.in_order_traversal(bt, results.add_result)
    print(results.results)


if __name__ == '__main__':
    test_reconstruct_bt()
