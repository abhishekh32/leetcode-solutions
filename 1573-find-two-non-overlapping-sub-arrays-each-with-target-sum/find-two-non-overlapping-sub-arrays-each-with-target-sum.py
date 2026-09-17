class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        INF = float('inf')
        best = [INF] * n

        left = 0
        curr_sum = 0
        answer = INF
        min_len = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Combine with a previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                # This is the best subarray ending at or before right
                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if answer == INF else answer