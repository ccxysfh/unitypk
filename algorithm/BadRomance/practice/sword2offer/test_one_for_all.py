#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: test_one_for_all.py
@time: 2018/9/5 09:58
"""
import unittest


class MyTestCase(unittest.TestCase):
    def tearDown(self):
        self.test_object = None

    def setUp(self):
        self.test_object = None

    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
