from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        if n == 1:
            return 0
        
        
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
        
        queue = deque([0])
        visited = set([0])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                i = queue.popleft()
                
                
                if i == n - 1:
                    return steps
                
                if i + 1 < n and i + 1 not in visited:
                    visited.add(i + 1)
                    queue.append(i + 1)
                
                
                if i - 1 >= 0 and i - 1 not in visited:
                    visited.add(i - 1)
                    queue.append(i - 1)
                
                
                for j in graph[arr[i]]:
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)
                
                
                graph[arr[i]].clear()
            
            steps += 1
        
        return -1