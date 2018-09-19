#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: three_six_zero.py
@time: 2018/9/17 20:37
"""

def change_k(n ,k):
    """

    Args:


    Returns:

    """
    pass


def min_num_of_max_k(k, l, r):
    times = 1
    mod = k
    if mod - 1 > r:
        return -1

    while mod <= r:
        mod *= k
        times = times + 1

    if r == k**(times) - 1:
        return r

    return k**(times-1)-1



# print(min_num_of_max_k(10, 1, 1000))


klist = [str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']


def mostLong(start, end, k):
    if start > end:
        return 0
    minnum = numLength(start, k)
    maxnum = numLength(end, k)
    maxlen = len(maxnum)
    minlen = len(minnum)
    pre = 0
    index = klist[k-1]
    for i in range(minlen, maxlen+1):
        temp = int(index*i, k)
        if temp <= int(maxnum, k) and temp >= int(minnum, k):
            pre = temp
    return pre


def numLength(num, k):
    cnt = []
    while num > 0:
        cnt.append(klist[num % k])
        num = num // k
    cnt.reverse()
    return ''.join(cnt)


# q = int(input())
# for i in range(q):
#     k, start, end = map(int, input().split())
#     print(mostLong(start, end, k))


# print(int('13', 8))
print(mostLong(1, 99, 10))


if __name__ == '__main__':
    pass
