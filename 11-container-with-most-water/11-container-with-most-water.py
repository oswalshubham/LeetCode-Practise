class Solution:
    def maxArea(self, height: List[int]) -> int:
        result= 0
        p=0
        q=len(height)-1
        
        while p<q:
            left = height[p]
            right = height[q]
            area = min(left,right)*(q-p)
            if area>result:
                result = area
                
            if left<right:
                p+=1
            else:
                q-=1
                
        return result
        