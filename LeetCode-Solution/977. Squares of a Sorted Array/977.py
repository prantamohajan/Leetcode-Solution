class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        answer = collections.deque()
        
       
        l, r = 0, len(nums) - 1
        
        while l <= r:
            
            left_val, right_val = abs(nums[l]), abs(nums[r])
            
            if left_val > right_val:
                
                answer.appendleft(left_val * left_val)
                l += 1
            else:
                
                answer.appendleft(right_val * right_val)
                r -= 1
                
        
        return list(answer)