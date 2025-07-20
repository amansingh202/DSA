class Solution:
    def infix_to_prefix(self, infix: str) -> str:
        # Step 1: Reverse the infix expression
        infix = infix[::-1]

        # Step 2: Swap brackets
        infix = list(infix)
        for i in range(len(infix)):
            if infix[i] == ')':
                infix[i] = '('
            elif infix[i] == '(':
                infix[i] = ')'
        infix = "".join(infix)

        stack = []
        ans = ""

        def pri(op):
            if op == '^':
                return 3
            elif op in ('*', '/'):
                return 2
            elif op in ('+', '-'):
                return 1
            else:
                return 0

        for ch in infix:
            if ch.isalnum():
                ans += ch
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    ans += stack.pop()
                if stack:
                    stack.pop()
            else:
                while (stack and pri(ch) < pri(stack[-1])) or \
                      (stack and pri(ch) == pri(stack[-1]) and ch != '^'):
                    ans += stack.pop()
                stack.append(ch)

        while stack:
            ans += stack.pop()

        return ''.join(reversed(ans))


obj = Solution()

print(obj.infix_to_prefix("(a+b)*c"))