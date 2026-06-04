class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int], waterStartTime: list[int], waterDuration: list[int]) -> int:
        
        minLandFinish = float('inf')
        for startTime, rideDuration in zip(landStartTime, landDuration):
            finishTime = startTime + rideDuration
            if finishTime < minLandFinish:
                minLandFinish = finishTime
        
        caseOneResult = float('inf')
        for startTime, rideDuration in zip(waterStartTime, waterDuration):
            finishTime = max(minLandFinish, startTime) + rideDuration
            if finishTime < caseOneResult:
                caseOneResult = finishTime
                
        minWaterFinish = float('inf')
        for startTime, rideDuration in zip(waterStartTime, waterDuration):
            finishTime = startTime + rideDuration
            if finishTime < minWaterFinish:
                minWaterFinish = finishTime
                
        caseTwoResult = float('inf')
        for startTime, rideDuration in zip(landStartTime, landDuration):
            finishTime = max(minWaterFinish, startTime) + rideDuration
            if finishTime < caseTwoResult:
                caseTwoResult = finishTime
                
        return min(caseOneResult, caseTwoResult)