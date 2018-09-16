#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: binary_search_tree.py
@time: 2018/5/16 19:56
"""

"""
bst
"""


class BinaryTreeNode(object):
    
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.val)
        

class BinarySearchTree(object):
    
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError("data can't be none")
        if self.root is None:
            self.root = BinaryTreeNode(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return BinarySearchTree(data)
        if data < node.val:
            if node.left is None:
                node.left = BinaryTreeNode(data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)

#  3(in\pre\post_order) dfs of tree


class Traversal(object):

    def __init__(self):
        pass

    def in_order_traversal(self, node, visit_func):
        """
        left root right
        """
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        """
        root left right
        """
        if node is not None:
            visit_func(node)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self, node, visit_func):
        """
        left right root
        """
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node)


class AllTraversal(object):

    def preorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []

        def _preorder(root, ret):
            ret.append(root.val)
            if root.left:
                _preorder(root.left, ret)
            if root.right:
                _preorder(root.right, ret)

        # _preorder(root, ret)
        # return ret

        def _preorder_loop(root, ret):
            stack = []
            stack.append(root)
            while stack:
                item = stack.pop()
                ret.append(item.val)
                if item.right:
                    stack.append(item.right)
                if item.left:
                    stack.append(item.left)

        def _preorder_loop2(root, ret):
            stack = []
            p = root
            while stack or p:
                if p is not None:
                    ret.append(p.val)
                    stack.append(p)
                    p = p.left
                else:
                    p = stack.pop()
                    p = p.right

        _preorder_loop(root, ret)
        return ret

    def inorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []

        def _inorder(root, ret):

            if root.left:
                _inorder(root.left, ret)
            ret.append(root.val)
            if root.right:
                _inorder(root.right, ret)

        def _inorder_loop(root, ret):
            stack = []
            p = root
            while stack or p:
                if p is not None:
                    stack.append(p)
                    p = p.left
                else:
                    p = stack.pop()
                    ret.append(p.val)
                    p = p.right
        return ret

    def postorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ret = []

        def _postorder(root, ret):

            if root.left:
                _postorder(root.left, ret)
            if root.right:
                _postorder(root.right, ret)

            ret.append(root.val)

        def _postorder_loop(root, ret):
            # ret 更精确的是使用链表，进行add_first操作，循环结束后，将ret反向
            p = root
            stack = []
            while stack or p:
                if p is not None:
                    stack.append(p)  # p 记录左子的指针
                    ret.append(p.val)
                    p = p.right
                else:
                    p = stack.pop()
                    p = p.left
            ret.reverse()

        return ret




if __name__ == '__main__':
    pass
