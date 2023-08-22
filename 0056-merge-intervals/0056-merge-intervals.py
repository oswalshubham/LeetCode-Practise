class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        merged = []
        intervals.sort()

        merged.append(intervals[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] > merged[-1][1]:
                merged.append(intervals[i])

            else:
                merged[-1][1] = max(intervals[i][1], merged[-1][1])

        return merged