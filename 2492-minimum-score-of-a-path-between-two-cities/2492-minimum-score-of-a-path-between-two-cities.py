class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = [i for i in range(n + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                parent[py] = px

        for u, v, _ in roads:
            union(u, v)

        root = find(1)
        res = float("inf")

        for u, v, w in roads:
            if find(u) == root:
                res = min(res, w)

        return res