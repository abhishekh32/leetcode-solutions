class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            # Opening bracket
            if ch in "([{":
                stack.append(ch)

            # Closing bracket
            else:
                if not stack:
                    return False

                top = stack[-1]

                if (ch == ')' and top != '(') or \
                   (ch == ']' and top != '[') or \
                   (ch == '}' and top != '{'):
                    return False

                stack.pop()

        return len(stack) == 0