class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        num = 0
        prev_oper = "+"

        s = s+ "+"

        '''
        25-15*5+50/2+
        [25,-75,25]
        '''
        for char in s:
            if char.isdigit():
                num = num*10+int(char)

            elif char in ["+", "-", "*", "/"]:
                if prev_oper == "+":
                    stack.append(num)

                elif prev_oper == "-":
                    stack.append(-num)

                elif prev_oper == "*":
                    top = stack.pop()
                    stack.append(top*num)

                elif prev_oper == "/":
                    top = stack.pop()
                    stack.append(math.trunc(top/num))

                prev_oper = char
                num = 0

        return sum(stack)

                
                

                



            

            

            
