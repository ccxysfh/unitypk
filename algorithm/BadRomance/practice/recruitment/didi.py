#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: didi.py
@time: 2018/9/18 19:56
"""
std_char1 = "q w e r t a s d f g z x c v".split(' ')
std_char2 = "y u i o p h j k l b n m".split(' ')
# print(len(std_char1) + len(std_char2))


def min_levenshtein_distance(a, b, ret):
    width = len(a) + 1  # column
    height = len(b) + 1  # row
    # 实例化python的矩阵确实麻烦
    lev_matrix = []
    for _ in range(height):
        row = []
        for _ in range(width):
            row.append(0)
        lev_matrix.append(row)

    for i in range(0, width):
        lev_matrix[0][i] = i
    for j in range(1, height):
        lev_matrix[j][0] = j

    for j in range(1, height):
        for i in range(1, width):
            indicator = 0 if a[i - 1] == b[j - 1] else 1
            if (a[i-1] in std_char1 and b[j-1] in std_char2) or (b[j-1] in std_char1 and a[i-1] in std_char2):
                indicator *= 2
            lev_matrix[j][i] = min(lev_matrix[j][i - 1] + 1*3,  # deletion
                                   lev_matrix[j - 1][i] + 1*3,  # insertion
                                   lev_matrix[j - 1][i - 1] + indicator)  # substitution
    distance = lev_matrix[height - 1][width - 1]
    if distance not in ret:
        ret[distance] = set()
        ret[distance].add(b)
    else:
        ret[distance].add(b)
    # ret[b] = lev_matrix[height - 1][width - 1]

import sys
words = list(input().split(' '))
std = words[0]
ret = {}
first = {}
for i, item in enumerate(words[1:]):
    first[item] = i

for item in words[1:]:
    min_levenshtein_distance(std, item, ret)
# print("ret:", ret)
sorted_keys = list(sorted(ret.keys()))
# print(sorted_keys)
# print(first)
result = []
for i in sorted_keys:
    total = len(ret[i]) + len(result)
    if total <= 3:
        for item in ret[i]:
            result.append(item)
    else:
        num = total - 3
        j = 0
        while j < num:

            min_key = sys.maxsize
            ele = None
            for item in ret[i]:
                if first[item] < min_key:
                    min_key = first[item]
                    ele = item
            result.append(ele)
            j += 1
        break
print(' '.join(result))


        # print(min_levenshtein_distance('slep', 'slap'))

if __name__ == '__main__':
    pass
