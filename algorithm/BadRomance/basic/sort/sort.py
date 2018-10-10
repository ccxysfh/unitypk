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
    Time: O(n^2) avarage, worst. O(1) best if input is already sorted.
    Space: O(1)

    In-place
    Stable
    small dataset
    每一个值r与左边所有的值比较，确定插入位置l，后面的[l:r]数据向后移一位
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
                    # 确定插入点l,缓存r位置值
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
        
"""
归并排序和快速排序的对比：在归并排序中，数据的划分是很快的，算法的主要运行时间在于合并子问题的解，
而在快速排序中，算法的主要工作在划分阶段，而不需要再去合并子问题的解了
"""
class MergeSort(object):
    """
    Complexity:
        Time: O(n log(n))
        Space: O(n)

    """
    def __init__(self, ):
        pass

    def sort(self, data):
        if data is None:
            raise TypeError('data can\'t be None')
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data

        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]
        left = self._sort(left)
        right = self._sort(right)
        return self._merge(left, right)

    def _merge(self, left, right):
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



class QucikSort(object):
    """Misc:
    * More sophisticated implementations are in-place, although they still take up recursion depth space
    * Most implementations are not stable

    See Quicksort on wikipedia:

    Typically, quicksort is significantly faster in practice than other Θ(nlogn) algorithms,
    because its inner loop can be efficiently implemented on most architectures[presumably because it has good cache locality],
    and in most real-world data, it is possible to make design choices which minimize the probability of requiring quadratic time.
    See: Quicksort vs merge sort: http://stackoverflow.com/a/90477"""
    def __init__(self, ):
        pass

    def sort(self, data):
        if data is None:
            raise TypeError('data can\'t be None')
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data
        pivot_index = len(data) // 2
        pivot = data[pivot_index]
        equal = []
        left = []
        right = []
        for item in data:
            if item == pivot:
                equal.append(item)
            elif item < pivot:
                left.append(item)
            else:
                right.append(item)
        left_ = self._sort(left)
        right_ = self._sort(right)

        return left_ + equal + right_

    # 标准的快排实现
    def partition_std(self, data, start, end):
        # 要进行上下限的限制
        if start >= end:
            return
        index = start
        l = start + 1
        r = end
        while l < r:

            while data[l] < data[index] and l < end:
                l += 1
            while data[r] > data[index] and r > start:
                r -= 1
            data[l], data[r] = data[r], data[l]

            # l += 1
            # r -= 1

        if l > end:
            l = end
        if r < start:
            r = start
        data[l], data[r] = data[r], data[l]
        data[index], data[r] = data[r], data[index]
        self.partition_std(data, start, r-1)
        self.partition_std(data, r+1, end)

    def quick_sort(self, array, left, right):
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            array[left] = array[right]
            while left < right and array[left] <= key:
                left += 1
            array[right] = array[left]
        array[right] = key
        self.quick_sort(array, low, left - 1)
        self.quick_sort(array, left + 1, high)

    # 算法导论实现
    def quick_sort_into(self, array, l, r):
        if l < r:
            q = self.partition(array, l, r)
            self.quick_sort_into(array, l, q - 1)
            self.quick_sort_into(array, q + 1, r)

    def partition(self, array, l, r):
        x = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1



def test_quick_sort():
    qs = QucikSort()
    # data = [9, 3, 1, 2, 1, 9]
    data = [5, 3, 1, 9, 8, 2, 4, 7]
    ret = qs.partition_std(data, 0, len(data)-1)
    print(data)

# test_quick_sort()








class RadixSort(object):  # 基排序

    def __init__(self, ):
        pass


class SelectionSort(object):
    
    def __init__(self, ):
        pass

    # method 1
    def sort(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data

        for i in range(len(data) - 1):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]
        return data

    # method 2
    def sort_iterative_alt(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            self._swap(data, i, self._find_min_index(data, i))
        return data

    def _find_min_index(self, data, start):
        min_index = start
        for i in range(start + 1, len(data)):
            if data[i] < data[min_index]:
                min_index = i
        return min_index

    def _swap(self, data, i, j):
        if i != j:
            data[i], data[j] = data[j], data[i]
        return data

    # method 3
    def sort_recursive(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if len(data) < 2:
            return data
        return self._sort_recursive(data, start=0)

    def _sort_recursive(self, data, start):
        if data is None:
            return
        if start < len(data) - 1:
            self._swap(data, start, self._find_min_index(data, start))
            self._sort_recursive(data, start + 1)
        return data






class HeapSort(object):
    """in-place
        not stable
    """

    def __init__(self, ):
        pass



class SortSolution(object):

    def __init__(self, ):
        pass

    def sort(self, nums):
        """
        original insert
        :param nums:
        :return:
        """
        # 从有序数组的第一个元素开始比较
        # for r in range(1, len(nums)):
        #     for l in range(r):
        #         if nums[r] < nums[l]:
        #             temp = nums[r]
        #             nums[l+1: r+1] = nums[l: r]
        #             nums[l] = temp
        # 从有序数组的最后一个元素开始比较
        for r in range(1, len(nums)):
            key = nums[r]
            for l in range(r-1, -1, -1):
                if nums[l] > key:
                    nums[l + 1] = nums[l]
                    nums[l] = key

    def sort(self, nums):
        """
        shell sort
        :param nums:
        :return:
        """
        pass

    def sort(self, nums):
        """
        bubble sort
        :param nums:
        :return:
        """
        # for i in range(len(nums)):  # 先排最大
        #     key = nums[0]
        #     for j in range(1, len(nums)-i):
        #         if key < nums[j]:
        #             key = nums[j]
        #         else:
        #             nums[j], nums[j-1] = nums[j-1], nums[j]
        # for i in range(len(nums)):  #  先排最小
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]
        for i in range(len(nums)-1):  #  先排最大
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]

    def sort(self, nums):
        """
        select
        :param nums:
        :return:
        """
        for i in range(len(nums)-1):
            mini = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[mini]:
                    mini = j
            nums[i], nums[mini] = nums[mini], nums[i]

    def _merge(self, left, right):
        l = 0
        r = 0
        ret = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                ret.append(left[l])
                l += 1
            else:
                ret.append(right[r])
                r += 1
        while l < len(left):
            ret.append(left[l])
            l += 1
        while r < len(right):
            ret.append(right[r])
            r += 1

        return ret

    def sort(self, nums):
        """
        merge sort
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return nums
        mid = len(nums) // 2
        left = self.sort(nums[:mid])
        right = self.sort(nums[mid:])

        return self._merge(left, right)



    def sort(self, nums, start, end):
        """
        quick
        :param nums:
        :param start:
        :param end:
        :return:
        """
        if start < end:
            piv_pos = self._partition(nums, start, end)
            self.sort(nums, start, piv_pos-1)
            self.sort(nums, piv_pos+1, end)

    def _partition(self, nums, start, end):
        position = start + 1
        pivot_pos = start
        for i in range(start+1, end+1):
            if nums[i] < nums[pivot_pos]:
                nums[position], nums[i] = nums[i], nums[position]
                position += 1
        position -= 1
        nums[position], nums[pivot_pos] = nums[pivot_pos], nums[position]
        return position

    def sort(self, nums):
        init_gap = len(nums) // 3
        while init_gap > 0:
            for i in range(init_gap, len(nums)):
                maxi = i
                for j in range(i, -1, -init_gap):
                    if nums[i] < nums[j]:
                        maxi = j
                nums[i], nums[maxi] = nums[maxi], nums[i]

            init_gap = init_gap // 2





def test_sort():
    ss = SortSolution()
    nums = [9, 3, 1, 0, 1, 9]
    # nums = [3,1, 2]
    print(ss.sort(nums))
    # print(ss.sort(nums, 0, len(nums)-1))
    print(nums)


if __name__ == '__main__':
    # sort = MergeSort()
    # data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
    # print(sort.sort(data))
    # print('start')
    test_sort()
