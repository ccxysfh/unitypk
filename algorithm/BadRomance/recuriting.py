#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: recuriting.py
@time: 2018/9/9 15:50
"""

def merge_set():
    temp = True
    count = 0
    while (temp and count < 5):
        (x, y) = (int(x) for x in input().split())
        ary1 = input().split()
        ary2 = input().split()
        ary1.extend(ary2)
        ary3 = []
        ary3 = [int(i) for i in ary1]
        ary4 = []
        ary4 = list(set(ary3))
        ary4.sort()
        ary5 = []
        ary5 = [str(i) for i in ary4]
        print(' '.join(ary5))
        count = count + 1


def change(t):
    table = dict()
    current = 97
    pattern = ''
    for item in t:
        if item in table:
            pattern += table[item]
        else:
            table[item] = chr(current)
            pattern += chr(current)
            current += 1
    return pattern


def new_change(s, t):
    table = {}
    for i in range(len(t)):
        if (s[i] not in table and t[i] in table.values()) or (s[i] in table and t[i] != table[s[i]]) :
            return False
        elif s[i] not in table:
            table[s[i]] = t[i]
    print(s)
    return True



def solve(S, T):
    # t_len = len(T)
    # s_len = len(S)
    #
    # pattern = change(T)
    # print(pattern)
    # count = 0
    # for i in range(s_len):
    #     if i + t_len <= s_len:
    #         current = S[i:i+t_len]
    #         current_change = change(current)
    #         if current_change == pattern:
    #             count += 1
    # return count
    t_len = len(T)
    s_len = len(S)

    count = 0
    for i in range(s_len):
        if i + t_len <= s_len:
            current = S[i:i + t_len]

            if new_change(current, T):
                count += 1
    return count

def test():
    s = 'ababcb'
    t = 'xyx'
    # s = 'abccdeefzzazff'
    # t = 'xyaa'
    print(solve(s, t))





"""
给定一张包含N个点、M条边的无向图，每条边连接两个不同的点，且任意两点间最多只有一条边。
对于这样的简单无向图，如果能将所有点划分成若干个集合，使得任意两个同一集合内的点之间没有边相连，
任意两个不同集合内的点之间有边相连，则称该图为完全多部图。现在你需要判断给定的图是否为完全多部图。
"""
def is_graph():
    count_num = int(input())
    count = 0
    while count < count_num:
        node_num, adjs_num = input().split(' ')
        adjs = []
        nodes = set()
        for i in range(adjs_num):
            adj = input().split(' ')
            adjs.append([int(adj[0]), int(adj[1])])
            nodes.add(int(adj[0]))
            nodes.add(int(adj[1]))




if __name__ == '__main__':
    # merge_set()
    test()