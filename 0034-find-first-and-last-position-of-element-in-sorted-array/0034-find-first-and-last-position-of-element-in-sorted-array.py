class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]

        def searchLeft():
            low = 0
            high = len(nums)-1

            index = -1
            '''
            [3,3,5,7,7,8,8,10,10,10]
                       s e   
                       m
            '''

            while low<=high:
                mid = low + (high-low)//2

                if nums[mid] > target:
                    high = mid-1

                elif nums[mid] < target:
                    low = mid+1

                else:
                    index = mid
                    high = mid-1

            return index
        
        def searchRight():
            index = -1
            low = 0
            high = len(nums)-1


            while low<=high:
                mid = low + (high-low+1)//2
                
                if nums[mid] > target:
                    high = mid-1

                elif nums[mid] < target:
                    low = mid+1

                else:
                    index = mid
                    low = mid+1

            return index


        return [searchLeft(),searchRight()]