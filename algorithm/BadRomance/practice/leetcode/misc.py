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


nums = [-1, 0, 1, 2, -1, -4]

# nums = [-1, 0, 1]

class ThreeSum(object):

    def __init__(self, ):
        pass

    def three_sum(nums):
        ret = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                curr = []
                count = nums[i] + nums[j]
                curr.append(nums[i])
                curr.append(nums[j])
                j += 1
                while j < len(nums):
                    count += nums[j]
                    curr.append(nums[j])
                    if count == 0 and len(curr) == 3:
                        tag = True
                        for item in ret:
                            if set(item) == set(curr[:]):
                                tag = False
                                break
                        if tag:
                            ret.append(curr[:])
                        curr.pop()
                        count -= nums[j]
                    elif len(curr) == 3:
                        count -= nums[j]
                        curr.pop()
                    j += 1

        return ret

    def three_sum_2(self, nums):
        lookup = {}
        ret = set()
        for i in nums:
            if i not in lookup:
                lookup[i] = 1
            else:
                lookup[i] += 1

        if 0 in lookup and lookup[0] > 2:
            ret.add((0, 0, 0))

        pos = [i for i in nums if i > 0]
        neg = [i for i in nums if i < 0]

        for p in pos:
            for n in neg:
                i = -p-n
                if i in lookup:
                    if i == 0 and lookup[i] > 0:
                        ret.add((n, i, p))
                    elif i == p and lookup[i] > 1:
                        ret.add((n, i, p))
                    elif i == n and lookup[i] > 1:
                        ret.add((n, i, p))
                    elif i > p and lookup[i] > 0:
                        ret.add((n, p, i))
                    elif i < n and lookup[i] > 0:
                        ret.add((i, n, p))
        return list(map(list, ret))

    def three_sum_3(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        ret = set()
        for i, x in enumerate(nums):
            cache = {}
            for y in nums[i+1:]:
                if y not in cache:
                    cache[-x-y] = 1
                else:
                    set.add((x, -x-y, y))
        return list(map(list, ret))




def test_three_sum():
    solution = ThreeSum()
    print(solution.three_sum_2(nums))



# print(three_sum((nums)))

class Solution:

    def __init__(self, ):
        self.mem = {}

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        return self.method1(price, special, needs)

    def cost_sum(self, price, needs):
        cost = 0
        for c, need in enumerate(needs):
            cost += need * price[c]
        return cost

    def method1(self, price, special, needs):
        if not price or not special or not needs:
            return 0
        cost = self.cost_sum(price, needs)
        for s in special:
            clone = needs[:]
            for c in range(len(clone)):
                if s[c] > clone[c]:
                    break
                clone[c] -= s[c]
            if c == len(needs)-1:
                cost = min(cost, s[-1] + self.method1(price, special, clone))
        return cost

def test():
    so = Solution()
    print(so.shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))







if __name__ == '__main__':
    # test_three_sum()
    test()