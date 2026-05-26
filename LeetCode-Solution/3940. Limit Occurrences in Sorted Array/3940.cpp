class Solution {
public:
    vector<int> limitOccurrences(vector<int>& nums, int k) {
       
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        vector<int> ans;
        int n = nums.size();
        if (n == 0) return ans;

        int count = 1; 
        ans.push_back(nums[0]);

        for (int i = 1; i < n; i++) {
            if (nums[i] == nums[i - 1]) {
                count++; 
            } else {
                count = 1; 
            }
            if (count <= k) {
                ans.push_back(nums[i]);
            }
        }

        return ans;
    }
};