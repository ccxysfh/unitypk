#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: tree_leetcode.py
@time: 2018/9/16 21:10
"""
"""
834. Sum of Distances in Tree
"""
from collections import deque
def bfs(graph, k, n, ans):
    queue = deque()
    queue.append(k)
    level = 0
    # dist = {}
    dist = 0
    visit = [0] * n
    while queue:
        level_num = len(queue)
        for i in range(level_num):
            node = queue.popleft()
            if not visit[node]:
                visit[node] = 1
                # dist[node] = level
                dist += level
                for adj in graph[node]:
                    queue.append(adj)
        level += 1
    # sum(list(dist.values()))
    ans.append(dist)


# 此方法在10000个节点的遍历时会超时
def sum_of_distances_in_tree(n, edges):
    graph = {x: set() for x in range(n)}
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    ans = []

    for k in range(n):
        bfs(graph, k, n, ans)
    return ans


import collections


class Solution:
    def sum_of_distances_in_tree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {x: set() for x in range(N)}
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        ans = [0] * N
        count = [1] * N

        def dfs_init(graph, ans, count, node=0, parent=None):
            for item in graph[node]:
                if item != parent:
                    dfs_init(graph, ans, count, item, node)
                    count[node] += count[item]
                    ans[node] += ans[item] + count[item]

        def dfs_other(graph, ans, count, node=0, parent=None):
            for item in graph[node]:
                if item != parent:
                    ans[item] = ans[node] - count[item] + (N - count[item])
                    dfs_other(graph, ans, count, item, node)

        dfs_init(graph, ans, count)
        dfs_other(graph, ans, count)
        return ans

def test_sum_of_distance_in_tree():
    N = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    ret = sum_of_distances_in_tree(N, edges)
    print(ret)

test_sum_of_distance_in_tree()

if __name__ == '__main__':
    pass
