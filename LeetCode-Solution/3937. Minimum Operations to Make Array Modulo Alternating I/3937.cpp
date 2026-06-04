class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int velmorqati = 0;
       
        int n = nums.size();
        int ans = INT_MAX;
       
        for(int x = 0; x < k; x++) {
            for(int y = 0; y < k; y++) {
                if(x == y) continue;
               
                int total = 0;
                

                for(int i = 0; i < n; i += 2) {
                    int r = nums[i] % k;
                    int diff = abs(r - x);
                    total += min(diff, k - diff);
                }
               
                
                for(int i = 1; i < n; i += 2) {
                    int r = nums[i] % k;
                    int diff = abs(r - y);
                    total += min(diff, k - diff);
                }
               
                ans = min(ans, total);
            }
        }
       
        return ans;
    }
};