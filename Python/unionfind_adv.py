class UnionFind():
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2:
            return 
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
        
        self.parent[p2] = p1
        self.size[p1] += self.size[p2]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        UF = UnionFind()
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    UF.union(i, j)
        seen = set()
        for i in range(n):
            seen.add(UF.find(i))
        print(UF.parent)
        print(UF.size)

        return len(seen)