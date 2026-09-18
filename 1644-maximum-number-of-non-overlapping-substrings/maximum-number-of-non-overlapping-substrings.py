class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)

        # First and last occurrence of each character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        # Build valid intervals
        for c in range(26):
            if first[c] == n:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                # This character appeared before l,
                # so we cannot create a valid substring starting at l.
                if first[x] < l:
                    valid = False
                    break

                # We must include all occurrences of this character.
                r = max(r, last[x])
                i += 1

            if valid:
                intervals.append((l, r))

        # Select maximum number of non-overlapping intervals.
        # Greedy: choose the interval with smallest ending index.
        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for l, r in intervals:
            if l > end:
                result.append(s[l:r + 1])
                end = r

        return result