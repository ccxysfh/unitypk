#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: misc.py
@time: 2018/9/16 10:30
"""
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
            ret += e+1
        elif curr[e] == 0:
            curr[e] = e
            ret += e+1
        else:
            curr[e] -= 1
    return ret
if __name__ == '__main__':
    pass
