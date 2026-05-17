class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int maxwater = 0;

        while (l < r) {
            int w = r - l;
            int h = min(height[l], height[r]);
            maxwater = max(maxwater, w * h);

            // move the smaller height pointer
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }

        return maxwater;
    }
};