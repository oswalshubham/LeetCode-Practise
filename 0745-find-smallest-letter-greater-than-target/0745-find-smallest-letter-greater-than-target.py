class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        low = 0
        high = len(letters)-1


        while low < high:
            mid = low+(high-low)//2

            if ord(letters[mid]) > ord(target):
                high = mid

            else:
                low = mid+1

        return letters[low] if ord(letters[low]) > ord(target) else letters[0]