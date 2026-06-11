class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        from typing import List
from collections import defaultdict

class Solution:
    MOD = 1_000_000_007

    def power(self, base: int, exponent: int) -> int:
        if exponent == 0:
            return 1

        half = self.power(base, exponent // 2)

        result = (half * half) % self.MOD

        if exponent % 2 == 1:
            result = (result * base) % self.MOD

        return result

    def getMaxDepth(self, adj, node: int, parent: int) -> int:
        depth = 0

        for neighbor in adj[node]:
            if neighbor == parent:
                continue

            depth = max(depth, self.getMaxDepth(adj, neighbor, node) + 1)

        return depth

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        maxDepth = self.getMaxDepth(adj, 1, 0)

        return self.power(2, maxDepth - 1)