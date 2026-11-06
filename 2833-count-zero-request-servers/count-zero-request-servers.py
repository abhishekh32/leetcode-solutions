from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])

        sorted_queries = sorted((q, i) for i, q in enumerate(queries))

        freq = {}
        ans = [0] * len(queries)

        left = right = 0
        active = 0

        for q, idx in sorted_queries:
            start = q - x

            # Add logs with time <= q
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if freq.get(server, 0) == 0:
                    active += 1

                freq[server] = freq.get(server, 0) + 1
                right += 1

            # Remove logs with time < q - x
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1
                    del freq[server]

                left += 1

            ans[idx] = n - active

        return ans