#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: misc.py
@time: 2018/9/16 10:30
"""
"""
617. Merge Two Binary Trees
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. 
Otherwise, the NOT null node will be used as the node of new tree.
合并两个二叉树，依次从跟节点开始遍历，如果节点位置重合，则加和两个节点的值作为新节点的值
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7

"""


class TreeNode(object):

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):

    def merge_trees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # t = TreeNode(0)
        # if t1 and t2:
        #     t.val = t1.val + t2.val
        #     t.left = self.merge_trees(t1.left, t2.left)
        #     t.right = self.merge_trees(t1.right, t2.right)
        # elif t1:
        #     t.val = t1.val
        #     t.left = self.merge_trees(t1.left, None)
        #     t.right = self.merge_trees(t1.right, None)
        # elif t2:
        #     t.val = t2.val
        #     t.left = self.merge_trees(None, t2.left)
        #     t.right = self.merge_trees(None, t2.right)
        # else:
        #     t = None
        if not t1 and not t2:
            return None

        val = (0 if t1 is None else t1.val) + (0 if t2 is None else t2.val)
        t = TreeNode(val)

        t.left = self.merge_trees(None if t1 is None else t1.left, None if t2 is None else t2.left)
        t.right = self.merge_trees(None if t1 is None else t1.right, None if t2 is None else t2.right)

        return t



"""
781 Rabbits in Forest（森林中的兔子
最多允许x+1只兔子同时回答x
使用一个hashmap记录当前状态，如果x不在hashmap中，将x+1加到result中，同时记录当前值x还能允许的回答x树目，如果数目大于0，减1即可，
否则将x+1加入到结果中，同时将hashmap中的x置为x，即还允许x只兔子回答x
Allow up to x+1 rabbits to answer x at the same time.
Use a hashmap(named curr)to record the current state,init ret = 0:
1. If x is not in the curr , add x+1 to ret, and record the current value curr[x]= x to allow x rabbits to answer x.
2. If the number curr[x] is greater than 0, curr[x] minus 1.
3. Otherwise curr[x]=0,  add x+1 to the ret, and set the curr[x]=x, which also allows x rabbits to answer x.
"""


def rabitss_in_forest(answers):
    ret, curr = 0, {}
    for e in answers:
        if e not in curr:
            curr[e] = e
            ret += e + 1
        elif curr[e] == 0:
            curr[e] = e
            ret += e + 1
        else:
            curr[e] -= 1
    return ret


if __name__ == '__main__':
    pass
