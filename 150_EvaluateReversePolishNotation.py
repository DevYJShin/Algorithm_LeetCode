class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                left = stack.pop()
                right = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    stack.append(int(left * 1.0 / right))

        return stack[-1]

# sol = Solution()
# test1 = ["2", "1", "+", "3", "*"]
# test2 = ["4", "13", "5", "/", "+"]
# test3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# print sol.evalRPN(test3)