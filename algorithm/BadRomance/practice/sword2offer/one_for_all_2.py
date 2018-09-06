#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_2.py
@time: 2018/9/5 09:57
"""
from basic.linked_list.linked_list import LinkedList, LinkedListNode
from basic.stack_queue.stack import Stack
from basic.tree.binary_search_tree import BinaryTreeNode, Traversal
from basic.utils.results import Results
"""
chapter 2
"""


"""
2 单例模式
"""


'''
3 二维数组中的查找
'''


'''
4 替换空格
'''

'''
5 从尾到头打印单链表
'''


def reverse_linked_list():
    linkedl = LinkedList()
    num_str = '123456'
    for item in num_str:
        linkedl.append(int(item))
    print(linkedl.get_all())

    stack = Stack()
    while linkedl.head:
        stack.push(linkedl.head.data)
        linkedl.head = linkedl.head.next
    while stack.head:
        print(stack.pop())


"""
6 重建二叉树
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


'''
7 用两个栈实现队列
'''


class QueueByStack(object):
    """
    use list as stack
    """
    def __init__(self, ):
        self.stack1 = []
        self.stack2 = []

    def push(self, data):
        if data is None:
            return
        if not self.stack1 and self.stack2:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
        else:
            self.stack1.append(data)

    def pop(self):
        if self.stack1 and not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def is_empty(self):
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False


def test_queue_by_stack():
    queue = QueueByStack()
    for item in 'a1b2c3':
        queue.push(item)

    while not queue.is_empty():
        print(queue.pop())


'''
8 旋转数组的最小数字
'''

'''
9 斐波那契数列
from basic.recursion_dynamic.fibonacci import Fibonacci, 求前n项和
这里列出一种生成器的方式输出序列
'''


def fib(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a+b


def test_fib():
    result = [item for item in fib(5)]
    print(result)


'''
10 二进制中1的个数
测试用例：正数、负数、0
'''


class CountOne(object):

    def __init__(self, ):
        pass

    def count_one(self, n: int):
        count = 0

        while n:
            # print(n)
            count += 1
            n = n & n-1
        return count


def test_count_one():
    n = 15
    count1 = CountOne()
    result = count1.count_one(n)
    print(result)


if __name__ == '__main__':
    # test_reconstruct_bt()
    # test_count_one()
    # reverse_linked_list()
    # test_queue_by_stack()
    # test_fib()
    test_count_one()
