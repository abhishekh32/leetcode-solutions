class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.size();

        int left = 0;
        int ones = 0;
        int bestLen = INT_MAX;
        string ans = "";

        for (int right = 0; right < n; right++) {
            if (s[right] == '1')
                ones++;

            // We have exactly k ones
            if (ones == k) {
                // Move left over unnecessary zeros
                while (s[left] == '0')
                    left++;

                int len = right - left + 1;
                string cur = s.substr(left, len);

                if (len < bestLen ||
                    (len == bestLen && cur < ans)) {
                    bestLen = len;
                    ans = cur;
                }

                // Remove the first '1' so we can find the next
                // group of k ones
                ones--;
                left++;
            }
        }

        return ans;
    }
};