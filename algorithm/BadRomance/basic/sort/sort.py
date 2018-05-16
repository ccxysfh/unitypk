#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: sort.py
@time: 2018/5/14 18:51
"""

class InsertionSort(object):
    """
    Time:O(n), O(n^2), O(n^2)
    小规模数据集
    """
    def __init__(self):
        pass

    def sort(self, data):
        if data is None:
            raise TypeError("data can't be None")
        if len(data) < 2:
            return data
        for r in range(1, len(data)):
            for l in range(r):
                if data[r] < data[l]:
                    temp = data[r]
                    data[l+1: r+1] = data[l: r]
                    data[l] = temp
        return data

    def sort_(self, data):
        if data is None:
            raise TypeError("data can't be None")
        for r in range(1, len(data)):
            self._insert(data, r, data[r])
        return data

    def _insert(self, data, pos, value):
        i = pos - 1
        while(i >= 0 and data[i] > value):
            data[i + 1] = data[i]
            i = i - 1
        data[i + 1] = value

class MedianSort(object):
    """
    Time：
    """
    def __init__(self, ):
        pass

    def sort(self):
        """
        """
        pass
        

class MergeSort(object):

    def __init__(self, ):
        pass

class QucikSort(object):

    def __init__(self, ):
        pass

class RadixSort(object):# 基排序

    def __init__(self, ):
        pass

class SelectionSort(object):
    
    def __init__(self, ):
        pass
    

class HeapSort(object):

    def __init__(self, ):
        pass






        
    

if __name__ == '__main__':
    pass