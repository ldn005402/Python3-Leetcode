class Solution:
    def calculate(self, s):
        for ch in ['+', '-', '(', ')']:
            s = s.replace(ch, ' ' + ch + ' ')
        sign = 1
        stack = [0]
        for token in s.split():
            if token in '+-':
                sign = 1 if token == '+' else -1
            elif token == '(':
                stack.extend([sign, 0])
                sign = 1
            elif token == ')':
                value = stack.pop() * stack.pop()
                stack[-1] += value
            else:
                stack[-1] += sign * int(token)
        return stack[-1]    
