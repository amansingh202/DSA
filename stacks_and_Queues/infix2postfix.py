class Solution:
    def infixToPostfix(self, s: str) -> str:
        def precedence(op):
            if op == '^':
                return 3
            elif op in ('*', '/'):
                return 2
            elif op in ('+', '-'):
                return 1
            else:
                return 0  # For '('

        def is_right_associative(op):
            return op == '^'

        stack = []
        ans = ""

        for char in s:
            if char.isalnum():  # Operand
                ans += char
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()  # pop '('
            else:  # Operator
                while (stack and stack[-1] != '(' and
                       (precedence(stack[-1]) > precedence(char))):
                    ans += stack.pop()
                stack.append(char)

        while stack:
            ans += stack.pop()

        return ans


obj = Solution()
print(obj.infixToPostfix("a+b*c")) 