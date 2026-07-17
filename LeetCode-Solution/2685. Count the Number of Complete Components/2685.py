from typing import List
from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        complete_components = 0
    
        for i in range(n):
            if not visited[i]:
                node_count = 0
                edge_count = 0
                queue = deque([i])
                visited[i] = True
                
                while queue:
                    curr = queue.popleft()
                    node_count += 1
                    edge_count += len(adj[curr])
                    
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                actual_edges = edge_count // 2
                
                if actual_edges == (node_count * (node_count - 1)) // 2:
                    complete_components += 1
                    
        return complete_components