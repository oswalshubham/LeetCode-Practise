class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        num = 0
        flag = False

        '''
        25+15*5+50/2
        [25,+,75,+,25]
        '''
        for char in s:
            if char.isdigit():
                num = num*10+int(char)

            elif char in ["+", "-", "*", "/"]:
                if flag:
                    sign = stack.pop()
                    a = stack.pop()

                    if sign == "*":
                        num = a*num
                    else:
                        num = a//num

                    flag = False
                
                if char in ["*", "/"]:
                    flag = True
                
                stack.append(num)
                if char == "+":
                    stack.append(1)
                elif char == "-":
                    stack.append(-1)
                else:
                    stack.append(char)

                num = 0

        if flag:
            sign = stack.pop()
            a = stack.pop()

            if sign == "*":
                num = a*num
            else:
                num = a//num

        stack.append(num)

        stack.reverse()
        while len(stack) > 1:
                a = stack.pop()
                sign = stack.pop()
                b = stack.pop()

                answer = a+b*sign

                stack.append(answer)

        return stack[-1]




            

            

            
