#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: tecent.py
@time: 2018/9/16 15:25
"""


def suba_in_b(suba, b, k):
    l = 0
    count = 0
    while l < len(b) - k + 1:
        if suba == b[l: l+k]:
            count += 1
        l += 1
    return count





# while True:
#     k = int(input())
#     A = input()
#     B = input()
#     # k = 2
#     # A = 'abab'
#     # B = 'ababab'
#     mem = {}
#     for i in range(len(A)):
#         if i <= len(A)-k:
#             if A[i: i+k] not in mem:
#                 mem[A[i: i+k]] = 1
#     count = 0
#     for suba in mem:
#         count += suba_in_b(suba, B, k)
#     print(count)
#     break
import math
def get_n_roud(x, y):
    return math.ceil(math.sqrt(2*(x+y))) - 1



def get_n(x, y):
    n_roud = get_n_roud(x, y)
    if n_roud*(n_roud + 1)/2 != (x+y):
        return -1
    print(n_roud)
    r = n_roud
    times = 0
    count = 0
    tag = False
    while r > 0:
        count += r
        times += 1
        if count == x:
            tag = True
            break
        elif count > x:
            count -= r
            times -= 1
            r -= 1
    return times if tag else -1

"""
2
"""

x, y = tuple(map(int, input().split(' ')))
print(get_n(x, y))


"""
3
"""


def is_triangle(a, b, c):
    # something here
    return False


def count_sum(x, y, z):
    # something here
    count = 0
    return count % 10000000007


x, y, z = tuple(map(int, input().split(' ')))
print(count_sum(x, y, z))


if __name__ == '__main__':
    pass
