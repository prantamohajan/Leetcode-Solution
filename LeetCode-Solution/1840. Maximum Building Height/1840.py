class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        
        restrictions.append([1, 0])
        restrictions.sort()
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
        m = len(restrictions)

        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i-1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i-1][1] + dist)
        for i in range(m - 2, -1, -1):
            dist = restrictions[i+1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1] + dist)
            
        max_height = 0
        for i in range(m - 1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_height = max(max_height, peak)
            
        return max_height