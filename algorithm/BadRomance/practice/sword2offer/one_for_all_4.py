#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_4.py
@time: 2018/9/6 15:53
"""
from basic.linked_list.linked_list import ComplexLinkedListNode
from basic.tree.binary_search_tree import BinarySearchTree, BinaryTreeNode
"""
chapter 4 
"""

"""
19 二叉树的镜像
"""

"""
20 顺时针打印矩阵
"""


class PrintMatrix(object):

    def __init__(self, ):
        self.result = []

    def print_matrix(self, matrix):
        if not matrix:
            return
        # loop time relate with rows and columns, We notice that the start coordinates are (0, 0), (1, 1)...
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        while rows > 2 * start and columns > 2 * start:
            self.print_circle(matrix, start, rows, columns, self.result)
            start += 1

    def print_circle(self, matrix, start, rows, cols, result):
        """
        确定每一层循环的
        """
        row = rows - 2 * start
        col = cols - 2 * start
        end_h = row + start - 1  # vertical
        end_w = col + start - 1  # horizon

        # left -> right
        for w in range(start, end_w + 1):
            result.append(matrix[start][w])
        # top -> bottom
        if start < end_h:
            for h in range(start + 1, end_h + 1):
                result.append(matrix[h][end_w])
        # right -> left
        if start < end_w and start < end_h:
            for w in range(start, end_w)[::-1]:
                result.append(matrix[end_h][w])
        # bottom -> top
        if start < end_w and start < end_h - 1:
            for h in range(start + 1, end_h)[::-1]:
                result.append(matrix[h][start])


def test_print_matrix():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    pm = PrintMatrix()
    pm.print_matrix(matrix)
    print(pm.result)


"""
21 包含min函数的栈
"""


class MinStack(object):
    # stack backed by list
    def __init__(self, ):
        self.data = []
        self.min = []

    def push(self, val):
        if not val:
            return
        self.data.append(val)
        if self.min and val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

    def pop(self):
        if self.data:
            self.min.pop()
            return self.data.pop()

    def min(self):
        return self.min[-1] if self.min else None


"""
22 栈的压入弹出序列
"""

"""
23 从上往下打印二叉树
即广度优先遍历二叉树
"""

"""
24 二叉树的后序遍历序列
判断一个序列是不是给定树的后续遍历，关注后序遍历的特性
"""


def is_post_order(order: list):
    if order is None or len(order) == 0:
        return False
    root = order[-1]
    left = 0
    while order[left] < root:
        left += 1
    right = left
    while right < len(order) - 1:
        if order[right] < root:
            return False
        right += 1
    is_left = True if left == 0 else is_post_order(order[:left])  # 左子序列为空, 因而left = 0
    is_right = True if left == right else is_post_order(order[left: right])  # 右子树为空，因而left==right
    return is_left and is_right


"""
25 二叉树中和为某一值的路径
二叉树中路径的和为某一固定值的所有路径
"""


class FindPathSum(object):

    def __init__(self, ):
        pass

    def find_path(self, bst_root, expected_sum):
        if bst_root is None:
            return
        path = []
        current_num = 0
        self._find_path(bst_root, expected_sum, path, current_num)

    def _find_path(self, bst_root, expected_sum, path, current_sum):
        is_leaf = bst_root.left is None and bst_root.right is None
        current_sum += bst_root.data
        path.append(bst_root.data)
        if current_sum == expected_sum and is_leaf:
            print(path)

        if bst_root.left is not None:
            self._find_path(bst_root.left, expected_sum, path, current_sum)
        if bst_root.right is not None:
            self._find_path(bst_root.right, expected_sum, path, current_sum)

        # cut current node from path and current value before returning to parent
        current_sum -= bst_root.data
        path.pop()


def test_find_path():
    from basic.tree.binary_search_tree import BinaryTreeNode
    root = BinaryTreeNode(10)
    node2 = BinaryTreeNode(5)
    node3 = BinaryTreeNode(12)
    node4 = BinaryTreeNode(4)
    node5 = BinaryTreeNode(7)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5

    fps = FindPathSum()
    fps.find_path(root, 22)


"""
26 复杂链表的复制
由于每个节点的额外指向不能确定是在前面还是后面，因而如果不采用额外的空间或者经历一次遍历之后，指向的节点可能还没有被复制
"""


class CloneComplexLinkedList(object):

    def __init__(self, ):
        pass

    def clone_complex_linkedlist(self, head: ComplexLinkedListNode):
        if head is None:
            return
        self._clone_linkedlist(head)
        self._construct_sibling(head)
        return self._split_linkedlist(head)

    def _clone_linkedlist(self, head: ComplexLinkedListNode):
        loop_node = head
        while loop_node:
            clone_node = ComplexLinkedListNode('a')
            clone_node.data = loop_node.data
            clone_node.next = loop_node.next
            clone_node.sibling = None  # can be removed( it is default)

            loop_node.next = clone_node
            loop_node = clone_node.next

    def _construct_sibling(self, head: ComplexLinkedListNode):
        loop_node = head
        while loop_node:
            if loop_node.sibling is not None:
                loop_node.next.sibling = loop_node.sibling.next
            loop_node = loop_node.next.next

    def _split_linkedlist(self, head: ComplexLinkedListNode):
        if head is None:
            return
        loop_node = head

        clone_head = clone_loop_node = loop_node.next
        loop_node.next = clone_loop_node.next
        loop_node = loop_node.next

        while loop_node:
            clone_loop_node.next = loop_node.next
            clone_loop_node = clone_loop_node.next
            loop_node.next = clone_loop_node.next
            loop_node = loop_node.next

        return clone_head
# test refer test_cloen_complex_linkedlist


"""
27 二叉搜索树与双向链表
将二叉搜索树转换成一个排序的双向链表
前序遍历可将搜索二叉树从小到大遍历
"""


class TransferBstToDoubleLinkedList(object):
    
    def __init__(self, ):
        pass

    def transfer(self, tree):
        if tree is None:
            return
        last_node = None
        root = tree.root
        self._construce(root, last_node)

        while last_node is not None and last_node.left is not None:
            last_node = last_node.left

        return last_node

    def _construce(self, node, last_node):
        current_node = node
        if current_node.left is not None:
            self._construce(current_node.left, last_node)

        current_node.left = last_node
        if last_node is not None:
            last_node.next = current_node
        last_node = current_node

        if current_node.right is not None:
            self._construce(current_node.right, last_node)


"""
28 字符串的排列
"""


class Permutation(object):
    
    def __init__(self, ):
        self.str_perm = []
        self.result = []

    def permutation(self, chars: str):
        for item in chars:
            chars_tmp = chars.replace(item, '')
            self.str_perm.append(item)
            if len(chars_tmp) > 0:
                self.permutation(chars_tmp)
            else:
                self.result.append(''.join(self.str_perm))
            self.str_perm.pop()


def test_permutation():
    chars = 'abc'
    p = Permutation()
    p.permutation(chars)
    print(p.result)
    

if __name__ == '__main__':
    # test_find_path()
    test_permutation()
