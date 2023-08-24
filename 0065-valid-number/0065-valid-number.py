import re

class Solution:
    def isNumber(self, s: str) -> bool:

        '''
        ^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$

        -23.5e2
        '''

        pattern = r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))([eE][+-]?\d+)?$"

        s = s.strip(" ")

        return re.match(pattern, s)
