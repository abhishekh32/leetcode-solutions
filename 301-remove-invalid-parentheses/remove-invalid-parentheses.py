class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        # Count how many '(' and ')' need to be removed
        remove_left = 0
        remove_right = 0

        for ch in s:
            if ch == '(':
                remove_left += 1

            elif ch == ')':
                if remove_left > 0:
                    remove_left -= 1
                else:
                    remove_right += 1

        result = set()

        def backtrack(index, current, balance, left_remove, right_remove):

            # Invalid: more ')' than '('
            if balance < 0:
                return

            # End of string
            if index == len(s):

                # Valid only if balance is 0
                # and we removed exactly what was required
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add("".join(current))

                return

            ch = s[index]

            # Option 1: Remove current '('
            if ch == '(' and left_remove > 0:
                backtrack(
                    index + 1,
                    current,
                    balance,
                    left_remove - 1,
                    right_remove
                )

            # Option 2: Remove current ')'
            if ch == ')' and right_remove > 0:
                backtrack(
                    index + 1,
                    current,
                    balance,
                    left_remove,
                    right_remove - 1
                )

            # Option 3: Keep current character
            current.append(ch)

            if ch == '(':
                backtrack(
                    index + 1,
                    current,
                    balance + 1,
                    left_remove,
                    right_remove
                )

            elif ch == ')':
                backtrack(
                    index + 1,
                    current,
                    balance - 1,
                    left_remove,
                    right_remove
                )

            else:
                # Letter
                backtrack(
                    index + 1,
                    current,
                    balance,
                    left_remove,
                    right_remove
                )

            current.pop()

        backtrack(
            0,
            [],
            0,
            remove_left,
            remove_right
        )

        return list(result)