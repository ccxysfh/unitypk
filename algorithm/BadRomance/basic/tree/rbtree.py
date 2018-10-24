#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: rbtree.py
@time: 2018/10/24 13:45
"""

BLACK = 0
RED = 1
# graphic elements of rbtree for printing
VC = '│'
HC = '─'
SIZE = 3
RIG = '┌' + HC * SIZE
LEF = '└' + HC * SIZE
SP = chr(32)
IND1 = SP * (SIZE + 1)
IND2 = VC + SP * SIZE


class rbnode(object):

    def __init__(self, key=None, value=None, color=BLACK):
        self.key = key
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.p = None

    def __repr__(self):
        return '%s%s%s' % (self.key, '◆' if self.color is BLACK else '◇', self.value)


class rbtree(object):

    def __init__(self, data=False, default_value=0):
        self.nil = rbnode()
        self.root = self.nil
        self.default_value = default_value  # for method: force_search
        if hasattr(data, '__iter__'):
            for key, value in data:
                self.insert(rbnode(key, value))

    def __repr__(self):
        return '\n'.join(self.graph())

    def graph(self, x=False, prefix=''):
        "beautifully print rbtree, big key node first"
        if x is False:
            x = self.root
        if x is not self.nil:
            p = x.p
            last_prefix = ''
            if p is not self.nil:
                pp = p.p
                last_prefix = LEF if p.left is x else RIG
                if pp is not self.nil:
                    if (pp.left is p) is (p.left is x):
                        prefix = prefix + IND1
                    else:
                        prefix = prefix + IND2
            yield from self.graph(x.right, prefix)
            yield '%s%s%s' % (prefix, last_prefix, x)
            yield from self.graph(x.left, prefix)

    def search(self, key, x=False):
        "find node according to key, return self.nil if not found"
        if x is False:
            x = self.root
        while (x is not self.nil) and (key != x.key):
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def insert(self, z):
        """
        将z置为红色，插入到树中对应位置，之后再重新调整颜色
        :param z:
        :return:
        """
        "insert z node with key and value"
        z.color = RED
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil

        self.insert_fixup(z)

    def delete(self, z):
        """
        先删除，再调整，如果左或右子一边为nil，则直接用另一子节点取代删除节点
        :param z:
        :return:
        """
        y = z
        y_original_color = y.color  # 记录待删除节点的颜色，如果是黑色需要重构
        if z.left is self.nil:
            x = z.right
            self.transplant(z, x)
        elif z.right is self.nil:
            x = z.left
            self.transplant(z, x)
        else:
            y = self.minimum(z.right)  # 顶位节点
            y_original_color = y.color
            x = y.right
            if y.p is z:
                x.p = y
            else:
                self.transplant(y, x)
                y.right = z.right
                y.right.p = y
            self.transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color  # 定位节点y继承删除节点的除了值以外的所有属性，包括颜色，如果顶位节点本身是红色，无需调整
        if y_original_color is BLACK:  # 删除的是黑色节点，则性质5不被满足，需要从删除节点处开始向上调整
            self.delete_fixup(x)

    def is_empty(self):
        return self.root is self.nil

    def right_walk(self, x=False):
        if x is False:
            x = self.root
        if x is not self.nil:
            yield from self.right_walk(x.right)
            yield x
            yield from self.right_walk(x.left)

    def left_walk(self, x=False):
        if x is False:
            x = self.root
        if x is not self.nil:
            yield from self.left_walk(x.left)
            yield x
            yield from self.left_walk(x.right)

    def force_search(self, key):
        y = self.nil
        x = self.root
        while x is not self.nil:
            if key == x.key:
                return x
            y = x
            if key < x.key:
                x = x.left
            else:
                x = x.right
        z = rbnode()
        original_z = z
        z.key = key
        z.value = self.default_value
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = self.nil
        z.right = self.nil
        z.color = RED
        self.insert_fixup(z)
        return original_z

    def maximum(self, x=False):
        if x is False:
            x = self.root
        while x.right is not self.nil:
            x = x.right
        return x

    def minimum(self, x=False):
        if x is False:
            x = self.root
        while x.left is not self.nil:
            x = x.left
        return x

    def successor(self, x):
        "return node with smallest key greater than x.key"
        if x.right is not self.nil:
            return self.minimum(x.right)
        y = x.p
        while (y is not self.nil) and (x is y.right):
            x = y
            y = y.p
        return y

    def predecessor(self, x):
        "return node with biggest key lower than x.key"
        if x.left is not self.nil:
            return self.maximum(x.left)
        y = x.p
        while (y is not self.nil) and (x is y.left):
            x = y
            y = y.p
        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.p = x
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        else:
            if x is x.p.left:
                x.p.left = y
            else:
                x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not self.nil:
            y.right.p = x
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        else:
            if x is x.p.right:
                x.p.right = y
            else:
                x.p.left = y
        y.right = x
        x.p = y

    def insert_fixup(self, z):
        while z.p.color is RED:
            if z.p is z.p.p.left:  # p为左子
                y = z.p.p.right
                if y.color is RED:  # 叔节点为红色，则只需要将父节点和叔节点置黑色，祖父节点置为红色
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p  # 循环判断祖父节点
                else:  # y为黑色或者nil都是黑色
                    if z is z.p.right:  # z若为右子，需要先左旋z.p
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = BLACK  # 左旋后父节点置黑，祖节点置红
                    z.p.p.color = RED
                    self.right_rotate(z.p.p)
            else:  # p为右子，逻辑相似对称
                y = z.p.p.left
                if y.color is RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z is z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotate(z.p.p)
        self.root.color = BLACK

    def delete_fixup(self, x):
        # 删除的解释参考https://blog.csdn.net/chinaleesunnyboy/article/details/79525456
        while (x is not self.root) and (x.color is BLACK):
            if x is x.p.left:
                w = x.p.right
                if w.color is RED:  # 情况1转情况2
                    w.color = BLACK
                    x.p.color = RED  # 置红结束循环
                    self.left_rotate(x.p)
                    w = x.p.right
                if (w.left.color is BLACK) and (w.right.color is BLACK):  # 情况2
                    w.color = RED
                    x = x.p
                else:
                    if w.right.color is BLACK:  # 情况3转情况4
                        w.left.color = BLACK  # 此时右子为black，左子为red，w为黑色，交换w和其左子的颜色
                        w.color = RED
                        self.right_rotate(w)  # w右旋，不改变红黑树性质
                        w = x.p.right
                    w.color = x.p.color  # 情况4
                    x.p.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.p)
                    x = self.root  # 结束循环
            else:
                w = x.p.left
                if w.color is RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.right_rotate(x.p)
                    w = x.p.left
                if (w.right.color is BLACK) and (w.left.color is BLACK):
                    w.color = RED
                    x = x.p
                else:
                    if w.left.color is BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.p)
                    x = self.root
        x.color = BLACK

    def transplant(self, u, v):
        if u.p is self.nil:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p


if __name__ == '__main__':
    trd = {'a': 7, 'b': 1, 'c': 8, 'd': 2, 'e': 3}
    tr = rbtree(trd.items())
    print("after build from dict:")
    print(tr)
    for c in 'sfsdfsahfweruoiwejuckjdflsfj':
        nd = tr.force_search(c)
        nd.value += 1
    print("\nafter insert from a string:")
    print(tr)
    while tr.root != tr.nil:
        tr.delete(tr.root)
    print("\nafter delete all node:")
    print(tr)


