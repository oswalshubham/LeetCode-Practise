from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()
        queue = deque([0])

        while len(queue)>0:
            start = queue.pop()
            if start not in visited:
                for end in range(start+1,len(s)+1):
                    if s[start:end] in wordDict:
                        queue.appendleft(end)

                        if end == len(s):
                            return True

                visited.add(start)

        return False