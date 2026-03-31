def bellmanFord(V, edges, src):
    dist = [1e9] * V 
    dist[src] = 0

    for i in range(V):
        for edge in edges:
            u, v, w = edge 
            if dist[u] != 1e9 and dist[u] + w < dist[v]:
                # If vth relaxation, then there exists negative cycle
                if i == V-1:
                    return [-1]
                dist[v] = dist[u] + w
    return dist 

if __name__ == '__main__':
    V = 5
    edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]

    src = 0
    ans = bellmanFord(V, edges, src)
    print(' '.join(map(str, ans)))