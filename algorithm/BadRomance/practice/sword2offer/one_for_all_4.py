#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_4.py
@time: 2018/9/6 15:53
"""
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

"""
22 栈的压入弹出序列
"""

"""
23 从上往下打印二叉树
"""

"""
24 二叉树的后序遍历序列
"""

"""
25 二叉树中和为某一值的路径
"""

"""
26 复杂链表的复制
"""

"""
27 二叉搜索树与双向链表
"""

"""
28 字符串的排列
"""

if __name__ == '__main__':
    pass
