class Solution:
    def isValid(self, s: str) -> bool:

        map = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack.pop() != map[ch]:
                    return False
        return not stack