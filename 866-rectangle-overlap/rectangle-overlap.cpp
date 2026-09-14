class Solution {
public:
    bool isRectangleOverlap(vector<int>& rec1, vector<int>& rec2) {
        
        // Check if they overlap horizontally
        bool horizontal = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2]);

        // Check if they overlap vertically
        bool vertical = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3]);

        return horizontal && vertical;
    }
};