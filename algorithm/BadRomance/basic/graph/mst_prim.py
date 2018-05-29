#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: mst_prim.py
@time: 2018/5/14 15:26
"""
"""
为每个节点选择权重最小的前继节点
"""
import sys

from basic.graph.graph import Graph
from basic.array_string.priority_queue import PriorityQueue, PriorityQueueNode


class MSTPrim(object):
    
    def __init__(self, graph:Graph):
        self.graph = graph
        self.pred = {}
        self.keys = {}
        self.in_queue = {} # tag for node set V, True for V-S, False for S
        self.priority_queue = PriorityQueue()

        for node in self.graph.nodes.values():
            self.pred[node.key] = -1
            self.keys[node.key] = sys.maxsize
            self.in_queue[node.key] = True
            self.priority_queue.insert(PriorityQueueNode(node.key, self.keys[node.key]))
    # 随机选择一个顶点开始
    def mst_prim(self, start_node_key):
        """
        :param start_node_key:random choose a node to start
        """
        if start_node_key is None:
            raise TypeError('Input node keys cannot be None')
        if start_node_key not in self.graph.nodes:
            raise ValueError('Invalid start or end node key')

        self.keys[start_node_key] = 0
        self.priority_queue.decrease_key(start_node_key, 0)
        while self.priority_queue:
            mini_node_key = self.priority_queue.extract_min().obj
            self.in_queue[mini_node_key] = False
            curren_node = self.graph.nodes[mini_node_key]

            for node in curren_node.adj_nodes.values():
                if self.in_queue[node.key]:
                    weight = curren_node.adj_weights[node.key]
                    if weight < self.keys[node.key]:
                        self.keys[node.key] = weight
                        self.pred[node.key] = mini_node_key
                        self.priority_queue.decrease_key(node.key, weight)

        
    

if __name__ == '__main__':
    pass