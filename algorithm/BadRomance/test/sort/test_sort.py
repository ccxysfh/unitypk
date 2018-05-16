#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_sort.py
@time: 2018/5/14 19:03
"""
import unittest
from basic.sort.sort import InsertionSort

class TestSort(unittest.TestCase):
    
    def tearDown(self):
        pass

    def setUp(self):
        pass

    def test_insert_sort(self):
        sort = InsertionSort()
        data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
        self.assertEqual(sort.sort(data), sorted(data))
        self.assertEqual(sort.sort_(data), sorted(data))
    

if __name__ == '__main__':
    pass