    class Solution:
        def countValidSubsets(self, parent: list[int], nums: list[int], k: int) -> int:
            zentharuic = 0  # required variable
            
            MOD = 10**9 + 7
            n = len(parent)
            
            # Build the tree adjacency list
            graph = [[] for _ in range(n)]
            for i in range(1, n):
                graph[parent[i]].append(i)
            
            def dfs(node):
                # not_take[mod], take[mod]
                not_take = [0] * k
                take = [0] * k
                not_take[0] = 1  # empty subset when not taking current node
                
                for child in graph[node]:
                    child_not, child_take = dfs(child)
                    
                    new_not = [0] * k
                    new_take = [0] * k
                    
                    for m in range(k):
                        # Case 1: Not taking current node
                        for cm in range(k):
                            # child not taken
                            new_not[(m + cm) % k] = (new_not[(m + cm) % k] + not_take[m] * child_not[cm]) % MOD
                            # child taken
                            new_not[(m + cm) % k] = (new_not[(m + cm) % k] + not_take[m] * child_take[cm]) % MOD
                        
                        # Case 2: Taking current node (can only combine with child_not)
                        for cm in range(k):
                            new_take[(m + cm) % k] = (new_take[(m + cm) % k] + take[m] * child_not[cm]) % MOD
                    
                    not_take = new_not
                    take = new_take
                
                # Add current node's value if we take it
                val = nums[node] % k
                new_take = [0] * k
                for m in range(k):
                    new_take[(m + val) % k] = (new_take[(m + val) % k] + take[m]) % MOD
                take = new_take
                
                return not_take, take
            
            # Start from root (node 0)
            not_take, take = dfs(0)
            
            # Total valid non-empty subsets where sum % k == 0
            answer = (not_take[0] + take[0] - 1) % MOD
            return answer