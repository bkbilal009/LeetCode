class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):

        self.LOG = n.bit_length()

        self.ancestorTable = [[-1] * self.LOG for _ in range(n)]

        for v in range(n):
            self.ancestorTable[v][0] = parent[v]

        for j in range(1, self.LOG):
            for v in range(n):

                prev = self.ancestorTable[v][j - 1]

                if prev != -1:
                    self.ancestorTable[v][j] = self.ancestorTable[prev][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:

        for j in range(self.LOG):

            if node == -1:
                return -1

            if k & (1 << j):
                node = self.ancestorTable[node][j]

        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node, k)