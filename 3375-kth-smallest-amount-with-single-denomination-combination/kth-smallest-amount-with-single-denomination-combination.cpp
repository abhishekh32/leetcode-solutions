class Solution {
public:
    long long gcd(long long a, long long b) {
        while (b) {
            long long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    long long lcm(long long a, long long b, long long limit) {
        long long g = gcd(a, b);
        
        // Avoid overflow and values larger than limit.
        if (a / g > limit / b)
            return limit + 1;
        
        return (a / g) * b;
    }

    long long count(long long x, vector<int>& coins) {
        int n = coins.size();
        long long total = 0;

        for (int mask = 1; mask < (1 << n); mask++) {
            long long curLCM = 1;
            int bits = 0;
            bool tooLarge = false;

            for (int i = 0; i < n; i++) {
                if (mask & (1 << i)) {
                    bits++;

                    curLCM = lcm(curLCM, coins[i], x);

                    if (curLCM > x) {
                        tooLarge = true;
                        break;
                    }
                }
            }

            if (tooLarge)
                continue;

            long long cnt = x / curLCM;

            if (bits % 2 == 1)
                total += cnt;
            else
                total -= cnt;
        }

        return total;
    }

    long long findKthSmallest(vector<int>& coins, long long k) {
        long long left = 1;
        long long right = 1LL * (*min_element(coins.begin(), coins.end())) * k;

        while (left < right) {
            long long mid = left + (right - left) / 2;

            if (count(mid, coins) >= k)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }
};