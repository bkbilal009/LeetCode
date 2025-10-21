class Solution:
    def merge(self, intervals):
        
        intervals.sort()

        
        merged = []

        
        for current in intervals:
            
            if len(merged) == 0:
                merged.append(current)
            
            elif merged[-1][1] < current[0]:
                merged.append(current)
            
            else:
                merged[-1][1] = max(merged[-1][1], current[1])

        
        return merged
  