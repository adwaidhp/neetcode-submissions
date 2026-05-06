class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            elif i in "+-*/":
                if i=="+":
                    elt2 =stack.pop()
                    elt1 = stack.pop()
                    stack.append(elt1+elt2)
                elif i == "-":
                    elt2 =stack.pop()
                    elt1 = stack.pop()
                    stack.append(elt1-elt2)
                elif i == "*":
                    elt2 =stack.pop()
                    elt1 = stack.pop()
                    stack.append(elt1*elt2)
                elif i == "/":
                    elt2 =stack.pop()
                    elt1 = stack.pop()
                    stack.append(int(elt1/elt2))
        return stack[-1]


