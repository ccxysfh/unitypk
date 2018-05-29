#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: compress_string.py
@time: 2018/5/28 21:00
"""


class CompressString(object):
    
    def __init__(self, ):
        pass

    def compress(self, string):
        if string is None or not string:
            return string
        pre = string[0]
        count = 0
        result = ''
        for char in string:
            if char == pre:
                count += 1
            else:
                # char != pre
                result += self.append_result(pre, count)
                pre = char
                count = 1  # 1 not 0
        result += self.append_result(pre, count)
        return result if len(result) < len(string) else string

    def append_result(self, pre_char, count):
        return pre_char + (str(count) if count > 1 else '')
    

if __name__ == '__main__':
    pass
