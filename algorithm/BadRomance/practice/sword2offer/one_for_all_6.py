#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_6.py
@time: 2018/9/6 15:53
"""
from basic.tree.lca_tree import Node
"""
chapter 6
"""


"""
38 数字在排序数组中出现的次数
总是把数据的容量想象到非常大，使用二分查找
"""


class HowManyTimes(object):

    def __init__(self, ):
        pass

    def how_many_times(self, nums: list, objection):
        if nums is None or objection is None:
            return
        if not nums:
            return 0
        first_k = self._get_first_k(nums, len(nums), 0, len(nums)-1, objection)
        last_k = self._get_last_k(nums, len(nums), 0, len(nums)-1, objection)
        return last_k - first_k + 1

    def _get_first_k(self, nums, length, start, end, k):
        mid = (start + end) // 2

        if nums[mid] == k:
            if mid > 0 and nums[mid - 1] != k or mid == 0:
                return mid
            else:
                end = mid - 1
        elif nums[mid] < k:
            end = mid - 1
        else:
            start = mid + 1

        return self._get_first_k(nums, length, start, end, k)

    def _get_last_k(self, nums, length, start, end, k):
        mid = (start + end) // 2

        if nums[mid] == k:
            if mid < length - 1 and nums[mid+1] != k or mid == length - 1:
                return mid
            else:
                start = mid + 1

        elif nums[mid] < k:
            start = mid + 1
        else:
            end = mid - 1

        return self._get_last_k(nums, length, start, end, k)


"""
39 二叉树的深度
"""


class TreeDepth(object):
    
    def __init__(self, ):
        pass

    def tree_depth(self, root):
        if root is None:
            return
        return self._tree_depth(root)

    def _tree_depth(self, root):
        if root is None:
            return 0
        left = self._tree_depth(root.left)
        right = self._tree_depth(root.right)

        return left + 1 if left > right else right + 1

    def is_balance(self, root):
        if root is None:
            return True

        left = self._tree_depth(root.left)
        right = self._tree_depth(root.right)
        if abs(left - right) > 1:
            return False

        return self.is_balance(root.left) and self.is_balance(root.right)

    # 诚然后序遍历是一个很契合要求的思路，同样是递归的思路，却做到了自底向上的不重复计算
    def is_balance_2(self, root):
        depth = [-1]
        return self._is_balance_2(root, depth)

    def _is_balance_2(self, root, depth):
        if root is None:
            depth[0] = 0
            return True
        left = [-1]
        right = [-1]
        if self._is_balance_2(root.left, left) and self._is_balance_2(root.right, right):
            if abs(left[0] - right[0]) <= 1:
                depth[0] = left[0] + 1 if left[0] > right[0] else right[0] + 1
                return True
        return False


def test_tree_depth():
    node10 = Node(10)
    node5 = Node(5)
    node12 = Node(12)
    node3 = Node(3)
    node1 = Node(1)
    node8 = Node(8)
    node9 = Node(9)
    node18 = Node(18)
    node20 = Node(20)
    node40 = Node(40)

    node3.left = node1
    node3.right = node8
    node5.left = node12
    node5.right = node3
    node20.left = node40
    node9.left = node18
    node9.right = node20
    node10.left = node5
    node10.right = node9
    root = node10
    td = TreeDepth()
    print(td.tree_depth(root))
    node60 = Node(60)
    node80 = Node(80)
    node12.left = node60
    node18.right = node80
    print(td.is_balance(root), td.is_balance_2(root))
    print(td.tree_depth(root))


"""
40 数组中只出现一次的数字
（一个数组中除了两个数字外，其他的数字都出现了两次，找出这两个只出现一次的数）
如果数组中只有一个数字是单独的，其他都成对出现，那么对数组中的元素进行连续的异或运算，即可得到这个唯一值
把这两个单独的数字分成两组
"""


class TwoUniqueNum(object):

    def __init__(self, ):
        pass

    def two_unique_num(self, nums: list):
        if nums is None or not nums:
            return
        xor_result = self._xor(nums)
        binary_xor_result = bin(xor_result)
        length = len(binary_xor_result)
        first_one = binary_xor_result.find('1')
        tag = 2**(length - first_one - 1)
        left = []
        right = []
        for item in nums:
            if item & tag == tag:
                left.append(item)
            else:
                right.append(item)
        return [self._xor(left), self._xor(right)]

    def _xor(self, nums):
        result = nums[0]
        for item in nums[1:]:
            result ^= item
        return result


def test_two_unique_num():
    tun = TwoUniqueNum()
    test_cases = [[2, 4, 3, 6, 3, 2, 5, 5]]
    print(tun._xor(test_cases[0]))

    print(tun.two_unique_num(test_cases[0]))


"""
41 和为s的两个数字 VS 和为s的连续正数序列
"""




"""
42 翻转单词顺序与左旋转字符串
"""


"""
43 n个骰子的点数
"""

"""
44 扑克牌的顺子
"""

"""
45 圆圈中最后剩下的数字
"""

"""
46 求1+2...+n
"""


"""
47 不用加减乘除做加法
"""

"""
48 不能被继承的类
"""

if __name__ == '__main__':
    test_two_unique_num()
