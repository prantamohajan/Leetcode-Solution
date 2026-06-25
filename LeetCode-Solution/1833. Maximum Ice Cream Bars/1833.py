class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        
        count = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break
        
        return count


# নিজে টেস্ট করার জন্য
if __name__ == "__main__":
    sol = Solution()
    
    result = sol.maxIceCream([1, 3, 2, 4, 1], 7)
    print("Answer:", result)   # Expected: 4