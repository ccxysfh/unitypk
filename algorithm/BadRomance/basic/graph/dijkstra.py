#!/usr/bin/env python
# encoding: utf-8

# Time: O((V+E)logv) for min-heap-based depends on which priority queue you used
"""
@author: changxin
@mail: PyCharm
@file: dijkstra.py
@time: 2018/5/13 23:15
"""
import sys

from basic.array_string.priority_queue import PriorityQueue, PriorityQueueNode

"""
singleSourceShortest
有向有权图, 距离才是优先队列的key值，是优先级的度量
优势
劣势：不能够应用有负权的边
"""
class Dijkstra(object):
    
    def __init__(self, graph):
        self.graph = graph
        self.pred = {}
        self.dist = {}
        self.priority_queue = PriorityQueue()

        for node in self.graph.nodes.values():
            self.pred[node.key] = -1
            self.dist[node.key] = sys.maxsize
            self.priority_queue.insert(PriorityQueueNode(node.key, self.dist[node.key]))

    def dijkstra(self, start_node_key, end_node_key=None):
        if start_node_key is None:
            raise TypeError('Input node keys cannot be None')
        if start_node_key not in self.graph.nodes:
            raise ValueError('Invalid start or end node key')

        self.dist[start_node_key] = 0
        self.priority_queue.decrease_key(start_node_key, self.dist[start_node_key])

        while self.priority_queue:
            current_min = self.priority_queue.extract_min().obj
            current_node = self.graph.nodes[current_min]

            for node in current_node.adj_nodes.values():
                weight = current_node.adj_weights[node.key]
                new_weight = self.dist[current_node.key] + weight
                if new_weight < self.dist[node.key]:
                    self.dist[node.key] = new_weight
                    self.priority_queue.decrease_key(node.key, new_weight)
                    self.pred[node.key] = current_min

        # Walk backwards to determine the shortest path:
        # Start at the end node, walk the previous dict to get to the start node
        if end_node_key:
            return self.full_path(end_node_key)


    def full_path(self, end_node_key):
        reslut = []
        current_node_key = end_node_key
        while current_node_key != -1:
            reslut.append(current_node_key)
            current_node_key = self.pred[current_node_key]
        return reslut[::-1]


if __name__ == '__main__':
    pass