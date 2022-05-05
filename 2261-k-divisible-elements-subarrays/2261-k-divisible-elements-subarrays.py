class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        
        def helper(index,k, array, result_set):
            q=index
            
            while q<len(nums):
                if nums[q]%p == 0 and k>0:
                    k-=1
                
                elif nums[q]%p==0:
                    break
                
                array.append(nums[q])
                result_set.add(tuple(nums[index:q+1]))
                
                q+=1
                
        result_set = set()
        for i in range(len(nums)):
            helper(i,k,[],result_set)
        
        return len(result_set)
                    
            
                    
            
            
        