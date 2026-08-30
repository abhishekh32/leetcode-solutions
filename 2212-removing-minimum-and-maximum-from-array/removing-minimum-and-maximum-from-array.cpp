class Solution {
public:
    int minimumDeletions(vector<int>& nums) {

        int n = nums.size();

        int minIndex = 0;
        int maxIndex = 0;

        // Find positions of minimum and maximum
        for (int i = 1; i < n; i++) {

            if (nums[i] < nums[minIndex])
                minIndex = i;

            if (nums[i] > nums[maxIndex])
                maxIndex = i;
        }

        // Make minIndex the smaller index
        if (minIndex > maxIndex)
            swap(minIndex, maxIndex);

        // Option 1: remove both from front
        int front = maxIndex + 1;

        // Option 2: remove both from back
        int back = n - minIndex;

        // Option 3: remove min from front
        // and max from back
        int both = (minIndex + 1) + (n - maxIndex);

        return min({front, back, both});
    }
};