"""
Given a positively weighted connected graph of n nodes, determine the minimum distance from node 0 to node i, where 0 <= i  < n.

Time complexity: O(V + ELOGV)
"""

from collections import defaultdict
from heapq import heappop, heappush


def dijkstra(edges):
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((w, v))
        adj[v].append((w, u))

    minHeap = [(0, 0)]  # (weight, node)
    dist = {0: 0}

    while minHeap:
        node, weight = heappop(minHeap)
        for nei, nei_weight in adj[node]:
            if nei in dist and dist[nei] <= weight + nei_weight:
                continue
            dist[nei] = weight + nei_weight
            heappush(minHeap, (weight + nei_weight, nei))
    return dist
