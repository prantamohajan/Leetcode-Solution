from collections import defaultdict, deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = 20
        depth = [0] * (n + 1)
        parent = [[0] * (n + 1) for _ in range(LOG)]

        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    parent[0][nei] = node
                    queue.append(nei)

        for k in range(1, LOG):
            for v in range(1, n + 1):
                parent[k][v] = parent[k-1][parent[k-1][v]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for k in range(LOG):
                if (diff >> k) & 1:
                    u = parent[k][u]
            if u == v:
                return u
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]
            return parent[0][u]

        MOD = 10**9 + 7
        result = []
        for u, v in queries:
            l = lca(u, v)
            path_len = depth[u] + depth[v] - 2 * depth[l]
            if path_len == 0:
                result.append(0)
            else:
                result.append(pow(2, path_len - 1, MOD))

        return result