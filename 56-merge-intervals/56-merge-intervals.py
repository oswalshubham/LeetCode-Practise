class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        def sortbyIndex(interval : List):
            return interval[0]
        
        intervals.sort(key = sortbyIndex)
        
        merged = []
        
        for interval in intervals:
            if len(merged)==0 or merged[-1][1]< interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
            
        