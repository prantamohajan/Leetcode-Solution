import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        MOD = 10**9 + 7

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.max_depth = 0
        
        def dfs(node, parent, current_depth):
            if current_depth > self.max_depth:
                self.max_depth = current_depth
                
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, current_depth + 1)
                    

        dfs(1, -1, 0)

        if self.max_depth == 0:
            return 1
            
        return pow(2, self.max_depth - 1, MOD)