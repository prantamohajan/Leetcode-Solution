class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();

        for (int val : nums) {
            int fre = 0;

            for (int el : nums) {
                if (el == val) {
                    fre++;
                }
            }

            if (fre > n/2) {
                return val;
            }
        }

        return -1; 
    }
};