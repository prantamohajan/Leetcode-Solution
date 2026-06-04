class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        n = len(position)
        
        def can_place(min_dist):
            count = 1
            last_position = position[0]
            
            for i in range(1, n):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                    if count >= m:
                        return True
            return False
            
        low = 1
        high = position[-1] - position[0]
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans