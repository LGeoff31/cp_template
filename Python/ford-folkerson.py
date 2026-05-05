"""
Ford Fulkerson used to solve the maximum flow problem in a flow graph.
The algorithm iteratively finds an augmenting path which is from source to sink in a residual graph.
The residual graph is one created by subtracting (capacity - current flow) for forward edges + adding backward edge of current flow
The algo then increases the flow along the augmenting path by maximum amount, which is the minimum capacity of edges along that path.
Runs in O(max flow * E)

"""

from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph # residual graph
        self.row = len(graph)
    
    def bfs(self, s, t, parent): # gives existence of augmenting path
        visited = [False] * self.row
        queue = []
        queue.append(s)
        visited[s] = True 
        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True 
                    parent[ind] = u 
                    if ind == t:
                        return True 
        return False 

    def FordFulkerson(self, source, sink):
        parent = [-1] * self.row
        max_flow = 0
        while self.bfs(source, sink, parent): # while theres augmenting path
            path_flow = float('inf')
            s = sink 
            while s != source:
                path_flow = min(path_flow, self.graph[s][s])
                s = parent[s]
            max_flow += path_flow 
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow 
                v = parent[v]
        return max_flow
    
graph = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0; sink = 5
 
print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))

