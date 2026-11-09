from typing import List
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = []
        count = [0] * k

        # Fenwick Tree to track available servers
        bit = [0] * (k + 1)

        def update(i, delta):
            i += 1
            while i <= k:
                bit[i] += delta
                i += i & -i

        def prefix_sum(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        def find_kth(order):
            idx = 0
            step = 1 << (k.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= k and bit[nxt] < order:
                    order -= bit[nxt]
                    idx = nxt
                step >>= 1

            return idx

        # Initially all servers are free
        for i in range(k):
            update(i, 1)

        for i, time in enumerate(arrival):

            # Release servers that finished
            while busy and busy[0][0] <= time:
                _, server = heapq.heappop(busy)
                update(server, 1)

            total_free = prefix_sum(k)

            if total_free == 0:
                continue

            start = i % k

            # Available servers before start
            before = prefix_sum(start)

            # Find first free server >= start, or wrap around
            if total_free > before:
                server = find_kth(before + 1)
            else:
                server = find_kth(1)

            update(server, -1)
            count[server] += 1

            heapq.heappush(busy, (time + load[i], server))

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]