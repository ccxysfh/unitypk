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
from enum import Enum


class State(Enum):
    unvisited = 0  # 顶点还未访问
    visiting = 1  # 顶点已被访问，但还存在未访问的邻接顶点
    visited = 2  # 顶点已被访问，且所有邻接顶点都被访问


class Node(object):

    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}  # Key = key, val = Node
        self.adj_weights = {}  # Key = key, val = weight

    def add_neighbor(self, neighbor, weight=0):
        if neighbor is None or weight is None:
            raise TypeError('neighbor or weight cannot be None')
        self.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError('neighbor cannot be None')
        if neighbor.key not in self.adj_nodes:
            raise KeyError('neighbor not found')
        self.incoming_edges += 1
        del self.adj_nodes[neighbor.key]
        del self.adj_weights[neighbor.key]


class Graph(object):

    def __init__(self, ):
        self.nodes = {}

    def add_node(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise KeyError('Invalid key')
        self.add_edge(source_key, dest_key, weight)
        self.add_edge(dest_key, source_key, weight)

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