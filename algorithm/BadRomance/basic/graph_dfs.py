#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: graph_dfs.py
@time: 2018/5/13 16:12
"""
from basic.graph import Graph, State, Node

class GraphDfs(Graph):

    def __init__(self, ):
        super(GraphDfs, self).__init__()
        self.pred = {}
        self.discovered = {}
        self.finished = {}
        self.count = 0

    def dfs(self, root, visit_func):
        if root is None:
            return
        for node in self.nodes.values():
            self.pred[node.key] = -1
            self.discovered[node.key] = -1
            self.finished[node.key] = -1

        visit_func(self.nodes[root])
        # 针对非连通图而言
        for node in self.nodes.values():
            if node.visit_state == State.unvisited:
                visit_func(node)

    # 对于每一节点，访问开始时标记为灰色，递归访问完所有的邻接节点后标记为黑色
    def dfs_visit(self, current_node):
        current_node.visit_state = State.visiting
        self.count += 1
        self.discovered[current_node.key] = self.count
        for node in current_node.adj_nodes.values():
            if node.visit_state == State.unvisited:
                self.pred[node.key] = current_node.key
                self.dfs_visit(node)
        current_node.visit_state = State.visited
        self.count += 1
        self.finished[current_node.key] = self.count


if __name__ == '__main__':
    root = Node(0)
    graph_dfs = GraphDfs()
    # graph_dfs.pred[root.key] = -1
    # graph_dfs.dfs(root, graph_dfs.dfs_visit)
    graph_dfs.add_node(1)