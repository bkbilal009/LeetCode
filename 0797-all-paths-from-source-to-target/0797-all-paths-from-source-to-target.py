class Solution:
    def allPathsSourceTarget(self, graph):
        result = []

        def dfs(node, path):
            path.append(node)
            if node == len(graph) - 1:
                result.append(path[:])
            else:
                for next_node in graph[node]:
                    dfs(next_node, path)
            path.pop()

        dfs(0, [])
        return result