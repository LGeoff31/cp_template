class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent != y_parent:
            if self.rank[x_parent] < self.rank[y_parent]:
                self.parent[y_parent] = x_parent 
            elif self.rank[x_parent] > self.rank[y_parent]:
                self.parent[y_parent] = x_parent
            else:
                self.parent[y_parent] = x_parent
                self.rank[x_parent] += 1

def kruskals_mst(V, edges):
    edges = sorted(edges, key=lambda x: x[2])
    uf = UnionFind(V)
    cost = 0
    count = 0

    for x,y,w in edges:
        if uf.find(x) != uf.find(y): # they are seperate
            uf.union(x, y)
            cost += w
            count += 1
            if count == V-1:
                break 
    return cost

def main():
    edges = [[0, 1, 10], [1, 3, 15], [2, 3, 4], [2, 0, 6], [0, 3, 5]]
    print(kruskals_mst(4, edges))
main()
