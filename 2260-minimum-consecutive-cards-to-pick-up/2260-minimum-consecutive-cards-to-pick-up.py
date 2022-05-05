class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        minCount = float('inf')
        for i in range(len(cards)):
            card = cards[i]
            if card not in dic:
                dic[card] = i    
            else:
                j = dic[card]
                minCount = min(minCount, i-j+1)
                dic[card] = i
                
        return minCount if minCount!=float('inf') else -1
                
                    
        