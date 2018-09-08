#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: one_for_all_5.py
@time: 2018/9/6 15:53
"""
"""
chapter 5
"""


"""
29 数组中出现次数超过一半的数字

"""
def get_more_half_num(nums: list):
    record = dict()
    length = len(nums)/2
    for num in nums:
        record[num] = record[num] + 1 if record.get(0) else 1
        if record[num] > length:
            return num
    return


"""
30 最小的k个数
采用最大堆，堆中存储k个数，比最大数小则进行替换
"""

"""
31 连续子数组的最大和
采用动态规划
"""


def max_sub_array(nums):
    result = float('-inf')
    current = 0
    for num in nums:
        if current <= 0:
            current = num
        else:
            current += num
        result = max(current, result)
    return result


"""
32 从1到n整数中1出现的次数
十进制表示中1出现的次数
"""

"""
33 把数组排成最小的数
对于数组中的任意两个数m、n，定义一个新的比较关系，如果mn > nm, 则定义m>n
"""
from functools import cmp_to_key


class ArrayToMIn(object):
    
    def __init__(self, ):
        pass

    def my_cmp(self, num1, num2):
        return int(str(num1) + str(num2)) - int(str(num2) + str(num1))

    def array_to_min(self, nums: list):
        if not nums:
            return
        sorted_num = sorted(nums, key=cmp_to_key(self.my_cmp))
        print(sorted_num)
        return int(''.join([str(num) for num in sorted_num]))
    

def test_array_to_min():
    nums = [321, 3, 23]
    atm = ArrayToMIn()
    print(atm.array_to_min(nums))


"""
34 丑数
包含因子2，3，5的数称为丑数，求按顺序的第k个丑数
"""


class Ugly(object):
    
    def __init__(self, ):
        pass

    def is_ugly(self, num):
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        return True if num == 1 else False


    




"""
35 第一个只出现一次的字符
相关问题均使用hashtable
"""


class FirstUniqueChar(object):

    def __init__(self, ):
        pass

    def first_unique_char(self, chars):
        if chars is None:
            return
        table = dict()
        loc = dict()
        for no, item in enumerate(chars):
            if item in table:
                table[item] += 1
            else:
                table[item] = 1
                loc[item] = no
        first_place = float('inf')
        ret = None
        for item in table:
            if table[item] == 1 and loc[item] < first_place:
                first_place = loc[item]
                ret = item
        return ret


def test_first_unique_char():
    fuc = FirstUniqueChar()
    chars = ['abaccdeff', 'abaccbddff', '', 'abcdeacb']
    for item in chars:
        print(fuc.first_unique_char(item))


"""
36 数组中的逆序对
使用归并排序，并统计每个子分组及分组合并时各自的逆序对
"""


class ReversePairs(object):

    def __init__(self,):
        pass

    def get_pairs(self, nums: list):
        if nums is None or not nums:
            return
        temp = nums.copy()
        return self._pairs_core(temp, 0, len(temp)-1)

    def _pairs_core(self, copy, start, end):
        if start == end:  # 递归结束条件
            return 0

        mid = (end - start) // 2
        left = self._pairs_core(copy, start, start + mid)
        right = self._pairs_core(copy, start + mid + 1, end)

        count = 0
        l_end = start + mid
        r_end = end
        t = []  # 记录当前归并结果，逆序
        while l_end >= start and r_end >= (start + mid + 1):
            if copy[l_end] > copy[r_end]:
                count += r_end - start - mid
                t.append(copy[l_end])
                l_end -= 1
            else:
                t.append(copy[r_end])
                r_end -= 1
        while l_end >= start:
            t.append(copy[l_end])
            l_end -= 1

        while r_end >= (start + mid + 1):
            t.append(copy[r_end])
            r_end -= 1

        copy[start: end+1] = t[::-1]

        return left + count + right


def test_reverse_paris():
    nums = [[7, 5, 6, 4],
            [7],
            [],
            None,
            [5, 7]]
    rp = ReversePairs()
    for item in nums:
        print(rp.get_pairs(item))


"""
37 两个链表的第一个公共结点
"""


if __name__ == '__main__':
    # test_first_unique_char()
    test_reverse_paris()
