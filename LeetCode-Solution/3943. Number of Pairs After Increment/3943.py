from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        freq1 = {}
        for num in nums1:
            freq1[num] = freq1.get(num, 0) + 1
            
        M = len(nums2)
        B = max(1, int(M ** 0.5))
        num_blocks = (M + B - 1) // B
        
        blocks = [{} for _ in range(num_blocks)]
        lazy = [0] * num_blocks
        
        for i, v in enumerate(nums2):
            b = i // B
            bl = blocks[b]
            bl[v] = bl.get(v, 0) + 1
            
        res = []
        
        for q in queries:
            if q[0] == 1:
                _, l, r, val = q
                sb = l // B
                eb = r // B
                
                if sb == eb:
                    lz = lazy[sb]
                    lazy[sb] = 0
                    bl = blocks[sb]
                    bl.clear()
                    start_idx = sb * B
                    end_idx = min(M, start_idx + B)
                    for i in range(start_idx, end_idx):
                        curr = nums2[i] + lz
                        if l <= i <= r:
                            curr += val
                        nums2[i] = curr
                        bl[curr] = bl.get(curr, 0) + 1
                else:
                    lz = lazy[sb]
                    lazy[sb] = 0
                    bl = blocks[sb]
                    bl.clear()
                    start_idx = sb * B
                    end_idx = start_idx + B
                    for i in range(start_idx, end_idx):
                        curr = nums2[i] + lz
                        if i >= l:
                            curr += val
                        nums2[i] = curr
                        bl[curr] = bl.get(curr, 0) + 1
                        
                    for b in range(sb + 1, eb):
                        lazy[b] += val
                        
                    lz = lazy[eb]
                    lazy[eb] = 0
                    bl = blocks[eb]
                    bl.clear()
                    start_idx = eb * B
                    end_idx = min(M, start_idx + B)
                    for i in range(start_idx, end_idx):
                        curr = nums2[i] + lz
                        if i <= r:
                            curr += val
                        nums2[i] = curr
                        bl[curr] = bl.get(curr, 0) + 1
            else:
                tot = q[1]
                ans = 0
                for b in range(num_blocks):
                    bl = blocks[b]
                    if not bl:
                        continue
                    lz = lazy[b]
                    
                    if len(freq1) < len(bl):
                        for u, f in freq1.items():
                            target = tot - u - lz
                            if target in bl:
                                ans += f * bl[target]
                    else:
                        for v, c in bl.items():
                            target = tot - v - lz
                            if target in freq1:
                                ans += c * freq1[target]
                res.append(ans)
                
        return res