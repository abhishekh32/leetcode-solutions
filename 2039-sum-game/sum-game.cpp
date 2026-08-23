class Solution {
public:
    bool sumGame(string num) {
        int n = num.size();
        int diff = 0;
        int qLeft = 0, qRight = 0;

        for (int i = 0; i < n / 2; i++) {
            if (num[i] == '?')
                qLeft++;
            else
                diff += num[i] - '0';
        }

        for (int i = n / 2; i < n; i++) {
            if (num[i] == '?')
                qRight++;
            else
                diff -= num[i] - '0';
        }

        // Same number of '?' on both sides.
        if (qLeft == qRight)
            return diff != 0;

        // Alice can force a win unless Bob can exactly compensate.
        return 2 * diff != 9 * (qRight - qLeft);
    }
};