UNVISITED = -1

n = number_of_nodes_in_graph
g = adjacency_list

id = 0
sccCount = 0

ids = [0] * n
low = [0] * n
onStack = [False] * n
stack = []


def findSccs():
    for i in range(n):
        ids[i] = UNVISITED
    for i in range(n):
        if ids[i] == UNVISITED:
            dfs(i)
    return low


def dfs(at):
    global id, sccCount

    stack.append(at)
    onStack[at] = True
    ids[at] = low[at] = id
    id += 1

    for to in g[at]:
        if ids[to] == UNVISITED:
            dfs(to)
        if onStack[to]:
            low[at] = min(low[at], low[to])

    if ids[at] == low[at]:
        while True:
            node = stack.pop()
            onStack[node] = False
            low[node] = ids[at]
            if node == at:
                break
        sccCount += 1
