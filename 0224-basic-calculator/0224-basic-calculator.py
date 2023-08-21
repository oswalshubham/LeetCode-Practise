class Solution:
    def calculate(self, s: str) -> int:

        stack = []

        result = 0
        sign = 1

        num = 0
        '''
        25-33+(50-2)
        '''


        for char in s:
            if char.isdigit():
                num = num*10+int(char)

            elif char in ["+", "-"]:
                result += num*sign

                num = 0

                if char == "+":
                    sign = 1
                else:
                    sign = -1

            elif char == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif char == ")":
                result = result + sign*num

                result = result*stack.pop()

                result = result + stack.pop()

                num = 0

        return result+num*sign


        