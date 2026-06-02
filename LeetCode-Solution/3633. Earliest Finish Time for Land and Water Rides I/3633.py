from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], 
                           waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_land_end = min(start + dur for start, dur in zip(landStartTime, landDuration))
        min_water_end = min(start + dur for start, dur in zip(waterStartTime, waterDuration))
        land_then_water = min(max(min_land_end, w_start) + w_dur 
                              for w_start, w_dur in zip(waterStartTime, waterDuration))
        water_then_land = min(max(min_water_end, l_start) + l_dur 
                              for l_start, l_dur in zip(landStartTime, landDuration))
        return min(land_then_water, water_then_land)