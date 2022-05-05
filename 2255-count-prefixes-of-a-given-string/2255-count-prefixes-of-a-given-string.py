class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for item in words:
            if s.startswith(item):
                count+=1
                
        return count
        