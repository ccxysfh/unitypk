#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: graph_leetcode.py
@time: 2018/9/16 09:20
"""

"""
310
剪枝法
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
从指定的根到叶节点的最长距离作为树的距离，因而最终可能的情况是内部的两个点或者是最中心的一个点
The actual implementation is similar to the BFS topological sort.
Remove the leaves, update the degrees of inner vertexes. 
Then remove the new leaves. 
Doing so level by level until there are 2 or 1 nodes left. 
"""
def find_min_height_tree(n, edges):
    if n == 1:
        return [0]
    degrees = [0]*n
    graph = {x: [] for x in range(n)}
    for e in edges:
        degrees[e[0]] += 1
        degrees[e[1]] += 1
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = [x for x in range(n) if degrees[x] == 1]  # 从叶节点进行剪枝

    while n > 2:
        n = n - len(queue)
        new_leaves = []
        for leave in queue:
            j = graph[leave].pop()  # 叶子只有一个邻接边
            graph[j].remove(leave)
            degrees[j] -= 1
            if degrees[j] == 1:
                new_leaves.append(j)
        queue = new_leaves

    return queue


def test_find_min_height():
    n = 7
    edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [5, 6]]
    ret = find_min_height_tree(n, edges)
    print(ret)

test_find_min_height()




if __name__ == '__main__':
    pass
