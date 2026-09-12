class Solution {
public:
    struct State {
        long long score = 0;
        vector<int> ids;
    };

    bool better(const State& a, const State& b) {
        if (a.score != b.score)
            return a.score > b.score;

        return a.ids < b.ids;   // lexicographically smaller
    }

    vector<int> maximumWeight(vector<vector<int>>& intervals) {
        int n = intervals.size();

        // Store: {left, right, weight, original_index}
        vector<array<int, 4>> a;

        for (int i = 0; i < n; i++) {
            a.push_back({
                intervals[i][0],
                intervals[i][1],
                intervals[i][2],
                i
            });
        }

        // Sort by starting point
        sort(a.begin(), a.end());

        // Find the first interval whose left > current right
        vector<int> next(n);

        for (int i = 0; i < n; i++) {
            int r = a[i][1];

            int lo = i + 1, hi = n;

            while (lo < hi) {
                int mid = lo + (hi - lo) / 2;

                if (a[mid][0] > r)
                    hi = mid;
                else
                    lo = mid + 1;
            }

            next[i] = lo;
        }

        // dp[k][i] = best answer using at most k intervals
        // from index i onward.
        vector<vector<State>> dp(5, vector<State>(n + 1));

        for (int i = n - 1; i >= 0; i--) {

            for (int k = 1; k <= 4; k++) {

                // Option 1: Don't take this interval
                State skip = dp[k][i + 1];

                // Option 2: Take this interval
                State take = dp[k - 1][next[i]];

                take.score += a[i][2];

                take.ids.push_back(a[i][3]);

                // We need indices in increasing order for
                // lexicographical comparison.
                sort(take.ids.begin(), take.ids.end());

                if (better(take, skip))
                    dp[k][i] = take;
                else
                    dp[k][i] = skip;
            }
        }

        return dp[4][0].ids;
    }
};