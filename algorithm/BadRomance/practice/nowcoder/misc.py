#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: misc.py
@time: 2018/9/11 17:56
"""
import sys


def dfs(graph, visit, node):
    height = len(graph)
    width = len(graph[0])
    visit[node] = 1
    for j in range(width):
        if node != j and visit[j] == 0 and graph[node][j]:
            dfs(graph, visit, j)


def main():
    std_input = input()
    while std_input:
        nodes_num, edge_nums = list(map(int, std_input.split(' ')))
        graph = []
        visit = []
        for i in range(nodes_num):
            row = []
            visit.append(0)
            for j in range(nodes_num):
                row.append(0)
            graph.append(row)

        for i in range(edge_nums):
            edge = tuple(map(int, input().split(' ')))
            graph[edge[0] - 1][edge[1] - 1] = graph[edge[1] - 1][edge[0] - 1] = 1
        count = 0
        for i in range(nodes_num):
            if not visit[i]:
                count += 1
                dfs(graph, visit, i)
            if count > 1:
                break
        if count == 1:
            print('YES')
        else:
            print('NO')
        a = [1, 2, 3]





from basic.graph.graph_dfs import GraphDfs
def main():
    while True:
        nodes_num, edge_nums = list(map(int, input()))
        graph = GraphDfs()
        for i in range(edge_nums):
            edge = tuple(map(int, input().split(' ')))
            graph.add_edge(edge[0], edge[1])





if __name__ == '__main__':
    main_2()
