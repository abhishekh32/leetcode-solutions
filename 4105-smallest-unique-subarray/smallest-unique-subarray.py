
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Build suffix array
        sa = list(range(n))
        rank = nums[:]
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for i in range(1, n):
                a = sa[i - 1]
                b = sa[i]

                prev = (
                    rank[a],
                    rank[a + k] if a + k < n else -1
                )

                curr = (
                    rank[b],
                    rank[b + k] if b + k < n else -1
                )

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        # Build inverse suffix array
        pos = [0] * n

        for i in range(n):
            pos[sa[i]] = i

        # Kasai's LCP algorithm
        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == n - 1:
                h = 0
                continue

            j = sa[r + 1]

            while (i + h < n and j + h < n
                   and nums[i + h] == nums[j + h]):
                h += 1

            lcp[r] = h

            if h > 0:
                h -= 1

        # Find minimum unique subarray
        ans = n

        for i in range(n):
            left = lcp[i - 1] if i > 0 else 0
            right = lcp[i]

            max_lcp = max(left, right)

            start = sa[i]
            remaining = n - start

            # A unique prefix must fit inside the suffix
            if max_lcp < remaining:
                ans = min(ans, max_lcp + 1)

        return ans
