#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: PyCharm
@file: graph.py
@time: 2018/5/13 15:20
"""

from enum import Enum


class State(Enum):
    unvisited = 0  # white，顶点还未访问
    visiting = 1  # gtey，顶点已被访问，但还存在未访问的邻接顶点
    visited = 2  # black，顶点已被访问，且所有邻接顶点都被访问


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


"""
图的其他表示方式，邻接表和邻接矩阵
邻接矩阵是对称的，
"""

if __name__ == '__main__':
    pass
