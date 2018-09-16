#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin
@mail: chengcx1019@gmail.com
@file: graph_traverse.py
@time: 2018/9/13 22:12
"""
from string import ascii_lowercase

"""
除了深度优先和广度优先遍历（参见graph_dfs和graph_bfs）之外，另外一个关于图遍历的应用是寻找图的连通分量
图的连通分量是图的一个最大子图，在这个子图中任何两个节点之间都是相互可达的。
与类表示的方式略有不同，这里采用的是邻接矩阵的方式存储图，visit[]数组对应具体节点的访问情况。
"""

def dfs(graph, visit, node):
    width = len(graph[0])
    visit[node] = 1
    for j in range(width):
        if node != j and visit[j] == 0 and graph[node][j]:
            dfs(graph, visit, j)


def main():
    graph = []
    visit = []
    k = int(input())
    count = 0
    while count < k:
        nodes_num, edge_nums = list(map(int, input().split(' ')))
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
        print(True) if count == 1 else print(False)


class stack(list):
    add = list.append

class ConnectedComponent(object):

    def __init__(self, ):
        pass

    def walk(self, G, s, S=set()):
        P, Q = dict(), set()  # Predecessors + "to do" queue
        P[s] = None  # s has no predecessor
        Q.add(s)  # We plan on starting with s
        while Q:  # Still nodes to visit
            u = Q.pop()  # Pick one, arbitrarily
            for v in G[u].difference(P, S):  # New nodes?
                Q.add(v)  # We plan to visit them!
                P[v] = u  # Remember where we came from
        return P

    def some_graph(self):
        a, b, c, d, e, f, g, h = range(8)
        N = [
            [b, c, d, e, f],  # a
            [c, e],  # b
            [d],  # c
            [e],  # d
            [f],  # e
            [c, g, h],  # f
            [f, h],  # g
            [f, g]  # h
        ]
        return N

    def component(self, G):
        comp = []
        visit = set()
        for u in G:
            if u in visit:
                continue
            C = self.walk(G, u)
            visit.update(C)
            comp.append(C)
        return comp

    def rec_dfs(self, G, s, S=None):
        if S is None:
            S = set()  # Initialize the history
        S.add(s)  # We've visited s
        for u in G[s]:  # Explore neighbors
            if u in S:
                continue  # Already visited: Skip
            self.rec_dfs(G, u, S)  # New: Explore recursively
        return S  # For testing

    def iter_dfs(self, G, s):
        S, Q = set(), []  # Visited-set and queue
        Q.append(s)  # We plan on visiting s
        while Q:  # Planned nodes left?
            u = Q.pop()  # Get one
            if u in S:
                continue  # Already visited? Skip it
            S.add(u)  # We've visited it now
            Q.extend(G[u])  # Schedule all neighbors
            yield u

    def tranerse(self, G, s, qtype=set):
        visit = set()
        queue = qtype()
        queue.add(s)
        while queue:
            u = queue.pop()
            if u in visit:
                continue
            visit.add(u)
            for v in G[u]:
                queue.add(v)
            yield u

    # Depth-First Search with Timestamps
    def dfs(self, G, s, d, f, S=None, t=0):
        if S is None:
            S = set()  # Initialize the history
        d[s] = t
        t += 1  # Set discover time
        S.add(s)  # We've visited s
        for u in G[s]:  # Explore neighbors
            if u in S:
                continue  # Already visited. Skip
            t = self.dfs(G, u, d, f, S, t)  # Recurse; update timestamp
        f[s] = t
        t += 1  # Set finish time
        return t  # Return timestamp

    # Topological Sorting Based on Depth-First Search
    def dfs_topsort(self, G):
        S, res = set(), []  # History and result

        def recurse(u):  # Traversal subroutine
            if u in S:
                return  # Ignore visited nodes
            S.add(u)  # Otherwise: Add to history
            for v in G[u]:
                recurse(v)  # Recurse through neighbors
            res.append(u)  # Finished with u: Append it  # finish time 越小相应发生在越后面

        for u in sorted(G.keys()):
            recurse(u)  # Cover entire graph
        res.reverse()  # It's all backward so far
        return res

    def tr(self, G):  # Transpose (rev. edges of) G
        GT = {}
        for u in G:
            GT[u] = set()  # Get all the nodes in there
        for u in G:
            for v in G[u]:
                GT[v].add(u)  # Add all reverse edges
        return GT

    def scc(self, G):
        GT = self.tr(G)  # Get the transposed graph
        sccs, seen = [], set()
        for u in self.dfs_topsort(G):  # DFS starting points
            if u in seen:
                continue  # Ignore covered nodes
            C = self.walk(GT, u, seen)  # Don't go "backward" (seen)
            seen.update(C)  # We've now seen C
            sccs.append(C)  # Another SCC found
        return sccs

    from string import ascii_lowercase
    def parse_graph(self, s):
        # print zip(ascii_lowercase, s.split("/"))
        # [('a', 'bc'), ('b', 'die'), ('c', 'd'), ('d', 'ah'), ('e', 'f'), ('f', 'g'), ('g', 'eh'), ('h', 'i'), ('i', 'h')]
        G = {}
        for u, line in zip(ascii_lowercase, s.split("/")):
            G[u] = set(line)
        return G



def test_connected_componebt():
    cc = ConnectedComponent()
    G = cc.some_graph()
    for i in range(len(G)):
        G[i] = set(G[i])

    print(list(cc.rec_dfs(G, 0)))  # [0, 1, 2, 3, 4, 5, 6, 7]
    print(list(cc.iter_dfs(G, 0)))
    print(list(cc.tranerse(G, 0)))
    discovered = {}
    finished = {}
    S = set()
    cc.dfs(G, 0, discovered, finished, S)
    print(S)
    G = {'a': set('bf'), 'b': set('cdf'), 'c': set('d'), 'd': set('ef'), 'e': set('f'), 'f': set()}
    print(cc.dfs_topsort(G))
    from collections import OrderedDict
    G = OrderedDict({'m': set('qrx'), 'n': set('oqu'), 'o': set('rsv'),
         'p': set('osz'), 'q': set('t'), 'r': set('uy'),
         's': set('r'), 't': set(), 'u': set('t'),
         'v': set('wx'), 'w': set('z'),
         'x': set(), 'y': set('v'), 'z': set()})
    print(cc.dfs_topsort(G))
    G = cc.parse_graph('bc/die/d/ah/f/g/eh/i/h')
    print(G)
    print(list(map(list, cc.scc(G))))
    # [['a', 'c', 'b', 'd'], ['e', 'g', 'f'], ['i', 'h']]

    """
    Python的list可以很好地充当stack，但是充当queue则性能很差，
    函数bfs中使用的是collections模块中的deque，即双端队列(double-ended queue)，
    它一般是使用链表来实现的，这个类有extend、append和pop等方法都是作用于队列右端的，
    而方法extendleft、appendleft和popleft等方法都是作用于队列左端的，它的内部实现是非常高效的。
    """





def answer_generator():
    for _ in range(5):
        yield print('yes')

def test_answer_generator():
    for answer in answer_generator():
        print(answer)





from graphviz import Graph, Digraph
class GraphTable:
    def __init__(self, nodes, edges, is_dir = False):
        self.nodes = nodes
        self.edges = edges
        self.is_dir = is_dir
        self.graph = []
        for node in nodes:
            self.graph.append([node])
        for edge in edges:
            for n in self.graph:
                if n[0] == edge[0]:
                    n.append(edge[1])
                if not is_dir:
                    if n[0] == edge[1]:
                        n.append(edge[0])
        self.G = None
    def __str__(self):
        return 'n'.join([str(n) for n in self.graph])
    def draw(self):
        settings = dict(name='Graph', engine='circo', node_attr=dict(shape='circle'), format='png')
        self.G = Digraph(**settings) if self.is_dir else Graph(**settings)
        for node in self.nodes:
            self.G.node(str(node), str(node))
        for edge in self.edges:
            self.G.edge(str(edge[0]), str(edge[1]))
        return self.G


# 加权图
class WeiGraph(GraphTable):
    def __init__(self, nodes, edges, is_dir=False):
        self.nodes = nodes
        self.edges = edges
        self.graph = []
        for node in nodes:
            self.graph.append([(node, 0)])
        for (x, y, w) in edges:
            for n in self.graph:
                if n[0][0] == x:
                    n.append((y, w))
                if not is_dir:
                    if n[0][0] == y:
                        n.append((x, w))
        self.G = None
        self.is_dir = is_dir
    def adjs(self, node):
        return list(filter(lambda n: n[0][0] == node, self.graph))[0][1:]
    def draw(self, color_filter=None):
        if color_filter is None:
            color_filter = lambda edge: 'black'
        settings = dict(name='Graph', engine='circo', node_attr=dict(shape='circle'))
        self.G = Graph(**settings) if not self.is_dir else Digraph(**settings)
        for node in self.nodes:
            self.G.node(str(node), str(node))
        for (x, y, w) in self.edges:
            self.G.edge(str(x), str(y), label=str(w), color=color_filter((x, y, w)))
        return self.G

gt = GraphTable([1,2,3,4,5], [(1,2), (1,5), (2,5), (2,4), (5,4), (2,3), (3,4)])
print(gt)
gt.draw()
"""
[1, 2, 5]
[2, 1, 5, 4, 3]
[3, 2, 4]
[4, 2, 5, 3]
[5, 1, 2, 4]
"""

if __name__ == '__main__':
    # test_answer_generator()
    # test_connected_componebt()
    pass
