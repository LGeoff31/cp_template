
def dfs1(v, visited, adj, st):
    visited[v] = True
    for nei in adj[v]:
        if not visited[nei]:
            dfs1(nei, visited, adj, st)
    st.append(v)

def dfs2(v, visited, adj, scc):
    visited[v] = True 
    scc.append(v)
    for nei in adj[v]:
        if not visited[nei]:
            dfs2(nei, visited, adj, scc)

def kosaraju(V, adj):
    # RUN DFS1
    visited = [False] * V
    st = []
    for i in range(V):
        if not visited[i]:
            dfs1(i, visited, adj, st)
    # REVERSE EDGES
    revAdj = [[] for _ in range(V)]
    for i in range(V):
        for v in adj[i]:
            revAdj[v].append(i)
    # RUN DFS2
    visited = [False] * V
    SCCs = []

    while st:
        node = st.pop()
        if not visited[node]:
            scc = []
            dfs2(node, visited, revAdj, scc)
            SCCs.append(scc)
    return SCCs

def main():
    V = 5
    edges = [[1,3], [3,2], [2,1], [1,4], [4,5]]
    adj = [[] for _ in range(V+1)]
    for u,v in edges:
        adj[u].append(v)

    SCCs = kosaraju(V+1, adj)
    print(SCCs)
    for i, scc in enumerate(SCCs):
        print(f"Strongly connected component #{i+1}", end=" ")
        for j in range(len(scc)):
            print(scc[j], end = " ")
        print()
main()