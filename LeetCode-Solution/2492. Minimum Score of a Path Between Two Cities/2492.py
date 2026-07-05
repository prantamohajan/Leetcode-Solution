from collections import deque
from math import inf
from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, distance in roads:
            adj[u].append((v, distance))
            adj[v].append((u, distance))
            
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        
        min_score = inf
        
        while queue:
            u = queue.popleft()
            
            for v, distance in adj[u]:
                if distance < min_score:
                    min_score = distance
                
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    
        return min_score