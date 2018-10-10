#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: avl.py
@time: 2018/5/16 21:17
"""
from collections import deque
#
# class AVLNode(object):
# 
#     def __init__(self, data=None):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.height = 0
# 
#     def compare_to(self, value):
#         """
#         Returns 0 if equal, negative if smaller and positive if greater.
#         Suitable for overriding.
#         """
#         if self.data == value:
#             return 0
#         if self.data < value:
#             return -1
#         return +1
# 
#     def rotate_right(self):
#         """LL, Perform right rotation around given node."""
#         new_root = self.left
#         grandson = new_root.right
#         self.left = grandson
#         new_root.right = self
# 
#         self.compute_height()
#         return new_root
# 
#     def rotate_left(self):
#         """Perform left rotation around given node."""
#         new_root = self.right
#         grandson = new_root.left
#         self.right = grandson
#         new_root.left = self
# 
#         self.compute_height()
#         return new_root
# 
#     def rotate_left_right(self):
#         """Perform left, then right rotation around given node."""
#         child = self.left
#         new_root = child.right
#         grand_left = new_root.left
#         grand_right = new_root.right
#         # rotate left
#         child.right = grand_left
#         new_root.left = child
#         # rotate right
#         self.left = grand_right
#         new_root.right = self
# 
#         child.compute_height()
#         self.compute_height()
#         return new_root
# 
#     def rotate_right_left(self):
#         """Perform right, then left rotation around given node."""
#         child = self.right
#         new_root = child.left
#         grand_left = new_root.left
#         grand_right = new_root.right
#         # rotate right
#         child.left = grand_right
#         new_root.right = child
# 
#         # rotate left
#         self.right = grand_left
#         new_root.left = self
# 
#         child.compute_height()
#         self.compute_height()
#         return new_root
# 
#     def add_to_subtree(self, parent, data):
#         if parent is None:
#             return self.new_node(data)
#         parent = parent.insert(data)
# 
#         return parent
# 
#     def insert(self, data):
#         if data is None:
#             raise TypeError("data is None")
# 
#         new_root = self
#         if self.compare_to(data) >= 0:
#             self.left = self.add_to_subtree(self.left, data)
#             if self.height_difference() == 2:
#                 if self.left.compare_to(data) >= 0:
#                     new_root = self.rotate_right()  # LL
#                 else:
#                     new_root = self.rotate_left_right()  # LR
#         else:
#             self.right = self.add_to_subtree(self.right, data)
#             if self.height_difference() == -2:
#                 if self.right.compare_to(data) < 0:
#                     new_root = self.rotate_left() # RR
#                 else:
#                     new_root = self.rotate_right_left() # RL
# 
#         new_root.compute_height()
#         return new_root
# 
#     def remove_from_parent(self, parent, data):
#         if parent:
#             return parent.remove(data)
#         return None
# 
#     def remove(self, data):
#         new_root = self
#         rs = self.compare_to(data)
#         if rs == 0:
#             if self.left is None:
#                 return self.right
# 
#             child = self.left
#             while child.right:
#                 child = child.right
# 
#             value = child.data
#             self.left = self.remove_from_parent(self.left, value)
#             self.data = value
# 
#             if self.height_difference() == -2:
#                 if self.right.height_difference() < 0:
#                     new_root = self.rotate_left()
#                 else:
#                     new_root = self.rotate_right_left()
#         elif rs > 0:
#             self.left = self.remove_from_parent(self.left, data)
#             if self.height_difference() == -2:
#                 if self.right.height_difference() < 0:
#                     new_root = self.rotate_left()
#                 else:
#                     new_root = self.rotate_right_left()
#         else:
#             self.right = self.remove_from_parent(self.right, data)
#             if self.height_difference() == 2:
#                 if self.left.height_difference >= 0:
#                     new_root = self.rotate_right()
#                 else:
#                     new_root = self.rotate_left_right()
# 
#         new_root.compute_height()
#         return new_root
# 
# 
#     def new_node (self, data):
#         """Return new Binary Node, amenable to subclassing."""
#         return AVLNode(data)
# 
#     def compute_height(self):
#         height = -1
#         if self.left:
#             height = max(height, self.left.height)
#         if self.right:
#             height = max(height, self.right.height)
# 
#         self.height = height + 1
# 
#     def dynamic_height(self):
#         height = -1
#         if self.left:
#             height = max(height, self.left.dynamic_height())
#         if self.right:
#             height = max(height, self.right.dynamic_height())
# 
#         return height + 1
# 
#     def height_difference(self):
#         left_target = 0
#         right_target = 0
#         if self.left:
#             left_target = 1 + self.left.height
#         if self.right:
#             right_target = 1 + self.right.height
# 
#         return left_target - right_target
# 
#     def dynamic_height_difference(self):
#         left_height = 0
#         right_height = 0
#         if self.left:
#             left_height = 1 + self.left.dynamic_height()
#         if self.right:
#             right_height = 1 + self.right.dynamic_height()
# 
#         return left_height - right_height
# 
#     def assert_avl_property(self):
#         """Validate AVL property for BST node."""
#         if abs(self.dynamic_height_difference()) > 1:
#             return False
#         if self.left:
#             if not self.left.assert_avl_property():
#                 return False
#         if self.right:
#             if not self.right.assert_avl_property():
#                 return False
#         return True
# 
#     def in_order (self):
#         """In order traversal generator of tree rooted at given node."""
#         if self.left:
#             for n in self.left.in_order():
#                 yield n
# 
#         yield self.data
# 
#         if self.right:
#             for n in self.right.in_order():
#                 yield n
# 
#     def pre_order(self):
#         yield self.data
# 
#         if self.left:
#             for n in self.left.pre_order():
#                 yield n
# 
#         if self.right:
#             for n in self.right.pre_order():
#                 yield  n
# 
#     def post_order(self):
# 
#         if self.left:
#             for n in self.left.post_order():
#                 yield n
# 
#         if self.right:
#             for n in self.right.post_order():
#                 yield  n
# 
#         yield self.data
# 
#     def bfs(self):
#         queue = deque()
#         queue.append(self)
# 
#         while queue:
#             node = queue.popleft()
#             yield node.data
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
# 
#     def __repr__ (self):
#         """Useful debugging function to produce linear tree representation."""
#         leftS = ''
#         rightS = ''
#         if self.left:
#             leftS = str(self.left)
#         if self.right:
#             rightS = str(self.right)
#         return "(L:" + leftS + " " + str(self.value) + " R:" + rightS + ")"
# 
# 
# 
# class AVLTree(object):
# 
#     def __init__(self):
#         self.root = None
# 
#     def __repr__ (self):
#         if self.root is None:
#             return "avl:()"
#         return "avl:" + str(self.root)
# 
#     def insert(self, data):
#         if data is None:
#             raise TypeError(data is None)
#         if self.root is None:
#             self.root = AVLNode(data)
#         else:
#             self.root = self.root.insert(data)
# 
#     def remove(self, data):
#         if self.root:
#             self.root = self.root.remove(data)
# 
#     def assert_avl_property(self):
#         if self.root:
#             return self.root.assert_avl_property()
#         else:
#             return True
# 
#     def __contains__(self, target):
#         if target is None:
#             raise TypeError("target is None")
#         node = self.root
#         while node:
#             rs = node.compare_to(target)
#             if rs > 0:
#                 node = node.left
#             elif rs < 0:
#                 node = node.right
#             else:
#                 return True
# 
#         return False


class AVLNode(object):
    """
    一旦节点的左右子树发生变更，就需要重新计算height，需要重新计算的节点的子树都不存在节点插入的情况，
    因而只要根据左右子树的高度就能计算出该节点的高度，使用compute_height()方法
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

    # 节点插入左子树左子节点
    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self

        # new_root会在外部重新计算高度，需要调整高度的只有当前节点self，
        self.compute_height()

        return new_root

    # 节点插入右子树右子节点
    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self

        # new_root会在外部重新计算高度，需要调整高度的只有当前节点self
        self.compute_height()

        return new_root

    # 节点插入左子树右子节点
    def rotate_left_right(self):
        # 首先以self.left为轴进行左旋转，构造插入左子树左节点的形状，之后再以self为轴进行右旋转
        # 新的root节点是self.left.right
        first_root = self.left
        new_root = first_root.right
        first_root.right = new_root.left
        new_root.left = first_root

        self.left = new_root.right
        new_root.right = self

        # new_root会在外部重新计算高度，需要调整高度的有当前节点self, 和first_root
        self.compute_height()
        first_root.compute_height()
        return new_root

    # 节点插入右子树左节点
    def rotate_right_left(self):
        # 首先以self.right为轴进行右旋转，构造插入右子树右子节点的形状，之后再以self为轴进行右旋转
        # 新的root节点是self.right.left
        first_root = self.right
        new_root = first_root.left
        first_root.left = new_root.right
        new_root.right = first_root

        self.right = new_root.left
        new_root.left = self

        # new_root会在外部重新计算高度，需要调整高度的有当前节点self, 和first_root
        self.compute_height()
        first_root.compute_height()
        return new_root

    def add_subtree(self, parent, value):
        if not parent:
            return AVLNode(value)
        parent = parent.insert(value)  # 插入完成后，root可能会发生变化，因而需要重新赋值
        return parent

    def insert(self, value):
        """
        判断新插入节点后到底属于哪种情况：
        挂载完新节点后，后从新节点的第一个父节点开始判断，该节点是否平衡，如不平衡，判断属于哪种情况的不平衡，
        根据value插入的是哪棵子树，并比较子树根节点和value的大小：
        1. 左子树left，且value < left.value: rotate_right右旋转
        2. 左子树left，且value > left.value: rotate_left_right 先左旋转，再右旋转
        3. 右子树right，且value > right.value: rotate_left右旋转
        4. 右子树right，且value < right.value: rotate_right_left 先右旋转，再左旋转
        """
        new_root = self
        if self.compare_to(value) > 0:
            self.left = self.add_subtree(self.left, value)
            if self.left.dynamic_difference() > 1:
                if self.left.compare_to(value) >= 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_left_right()
        else:
            self.right = self.add_subtree(self.right, value)
            if self.right.dynamic_difference() < -1:
                if self.right.compare_to(value) < 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()

        # 左右子树的height均已重新计算过
        new_root.compute_height()
        return new_root

    def remove_from_parent(self, parent, value):
        if parent:
            return parent.remove(value)
        return None

    def remove(self, value):
        """
        1. 叶节点直接删除
        2. 左右子树有一边为空，返回剩余一边
        3. 左右均不为空 删除的节点左右子树均不为空，那么用左子树最大的元素a（必为叶节点）替换被删除节点，然后递归删除a节点
        """
        new_root = self
        compare = self.compare_to(value)
        if compare == 0:
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            node = self.left
            while node:
                node = node.right
            most_left_key = node.value
            self.value = most_left_key
            self.left = self.remove_from_parent(self.left, most_left_key)
            if self.dynamic_differnece() == -2:  # 只可能左子树低于右子树
                if self.right.dynamic_differnece() < 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()
        elif compare < 0:
            self.right = self.remove_from_parent(self.right, value)
            if self.dynamic_difference() == 2:  # 只可能左子树高于右子树
                if self.left.dynamic_differnece() > 0:
                    new_root = self.rotate_right()
                else:
                    new_root = self.rotate_left_right()
        else:
            self.left = self.remove_from_parent(self.left, value)
            if self.dynamic_difference() == -2:  # 只可能左子树低于右子树
                if self.right.dynamic_differnece() < 0:
                    new_root = self.rotate_left()
                else:
                    new_root = self.rotate_right_left()
        new_root.compute_height()
        return new_root

    def compare_to(self, target):
        tag = 0
        if self.value < target:
            tag = -1
        elif self.value > target:
            tag = 1
        return tag

    def compute_height(self):
        height = -1
        if self.left:
            height = max(height, self.left.height)
        if self.right:
            height = max(height, self.right.height)

        self.height = height + 1

    def dynamic_height(self):
        height = -1
        if self.left:
            height = max(height, self.left.dynamic_height())
        if self.right:
            height = max(height, self.right.dynamic_height())

        return height + 1

    def compute_difference(self):
        left_target = 0
        right_target = 0
        if self.left:
            left_target = 1 + self.left.height
        if self.right:
            right_target = 1 + self.right.height

        return left_target - right_target

    def dynamic_difference(self):
        left_target = 0
        right_target = 0
        if self.left:
            left_target = 1 + self.left.dynamic_height()
        if self.right:
            right_target = 1 + self.right.dynamic_height()

        return left_target - right_target

    def assert_avl_property(self):
        if abs(self.dynamic_difference()) > 1:
            return False
        if self.left:
            if not self.assert_avl_property(self.left):
                return False
        if self.right:
            if not self.assert_avl_property(self.right):
                return False

        return True

    def bfs(self):
        queue = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()
            yield node.value
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


class AVLTree(object):

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not value:
            raise TypeError("value can't be None")
        if not self.root:
            self.root = AVLNode(value)
        else:
            self.root = self.root.insert(value)

    def remove(self, value):
        if not value:
            raise TypeError("value can't be None")
        if self.root:
            self.root = self.root.remove(value)

    def __contains__(self, target):
        if not target or not self.root:
            return False
        node = self.root
        while node:
            if node.compare_to(target) > 0:
                node = node.left
            elif node.compare_to(target) < 0:
                node = node.right
            else:
                return True
        return False


if __name__ == '__main__':
    avl = AVLTree()
    node_datas = [5, 2, 8, 1, 3, 4]
    for node_data in node_datas:
        avl.insert(node_data)
    print(list(avl.root.bfs()))
    avl.remove(3)
    print(list(avl.root.bfs()))