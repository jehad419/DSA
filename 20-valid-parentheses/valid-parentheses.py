class Solution:
    def isValid(self, s: str) -> bool:
        #Solved by Jehad Hasan
        stack = []

        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack) == 0