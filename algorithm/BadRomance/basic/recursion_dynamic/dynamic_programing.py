#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: dynamic_programing.py
@time: 2018/9/9 14:41
"""
"""
transfer from a to b
"""


class LevenshteinDistance(object):
    
    def __init__(self, ):
        pass

    def min_levenshtein_distance(self, a, b):
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
                indicator = 0 if a[i-1] == b[j-1] else 1
                lev_matrix[j][i] = min(lev_matrix[j][i-1] + 1,  # deletion
                                       lev_matrix[j-1][i] + 1,  # insertion
                                       lev_matrix[j-1][i-1] + indicator)  # substitution

        return lev_matrix[height-1][width-1]


def test_min_levenshtein_distance():
    solution = LevenshteinDistance()
    print(solution.min_levenshtein_distance('ME', 'MY'))
    print(solution.min_levenshtein_distance('Saturday', 'Sunday'))
    


if __name__ == '__main__':
    test_min_levenshtein_distance()
