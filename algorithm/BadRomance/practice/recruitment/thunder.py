#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: thunder.py
@time: 2018/9/12 19:17
"""
def find_num(array):
    left = 0
    right = len(array)
    count = 0
    ret = []
    while left < right - 1:
        count += array[left]
        if count == array[left+1]:
            right_count = 0
            if left + 2 <= right:
                for i in range(left+2, right):
                    right_count += array[i]
            if count == right_count:
                ret.append(array[left+1])
                count = 0

        left += 1

    return ret


# def main():
#     while True:
#         array = list(map(int, input().split(',')))
#         ret = find_num(array)
#         print(ret[0]) if ret else print('False')

def _sort(data):
    if len(data) < 2:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]
    left = _sort(left)
    right = _sort(right)
    return _merge(left, right)


def _merge(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1
    return result

while True:
    array1, array2_k = input().split('-')
    array2, k = array2_k.split(':')
    array1 = list(map(int, array1.split(',')))
    array2 = list(map(int, array2.split(',')))
    k = int(k)
    s1 = _sort(array1)
    s2 = _sort(array2)
    # print(sorted_array1, sorted_array2, k)
    left = len(s1) - 1
    right = len(s2) - 1
    ret = []
    l = left
    r = right
    ret.append()
    while l > 0:

        while r > 0:

            if s1[l] + s2[r-1] >= s1[l-1] + s2[r]:
                ret.append(s1[l] + s2[r-1])
                r -= 1
                if len(ret) == k:
                    break
            else:
                ret.append(s1[l-1] + s2[r])
                # 2,4,2,7,7-3,2,5,6,1,9:6








if __name__ == '__main__':
    pass
