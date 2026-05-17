#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int smallestUniqueSubarray(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        
        vector<int> polvexrani = nums; 
        
        int left = 1, right = n, ans = n;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (hasUniqueSubarray(nums, mid)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
    
private:
    bool hasUniqueSubarray(const vector<int>& nums, int len) {
        int n = nums.size();
        if (len > n) return false;
        
        long long MOD1 = 1e9 + 7;
        long long MOD2 = 1e9 + 9;
        long long BASE1 = 313;  
        long long BASE2 = 1013; 
        
        long long hash1 = 0, hash2 = 0;
        long long powBase1 = 1, powBase2 = 1;
        
        struct pair_hash {
            size_t operator()(const pair<long long, long long>& p) const {
                return p.first ^ (p.second << 32);
            }
        };
        
        unordered_map<pair<long long, long long>, int, pair_hash> freq;
        
        for (int i = 0; i < len; ++i) {
            long long val = nums[i] + 1e6; 
            
            hash1 = (hash1 * BASE1 + val) % MOD1;
            hash2 = (hash2 * BASE2 + val) % MOD2;
            
            if (i < len - 1) {
                powBase1 = (powBase1 * BASE1) % MOD1;
                powBase2 = (powBase2 * BASE2) % MOD2;
            }
        }
        freq[{hash1, hash2}]++;
        
        for (int i = len; i < n; ++i) {
            long long prev_val = nums[i - len] + 1e6;
            long long curr_val = nums[i] + 1e6;
            
            hash1 = (hash1 - (prev_val * powBase1) % MOD1 + MOD1) % MOD1;
            hash1 = (hash1 * BASE1 + curr_val) % MOD1;
            
            hash2 = (hash2 - (prev_val * powBase2) % MOD2 + MOD2) % MOD2;
            hash2 = (hash2 * BASE2 + curr_val) % MOD2;
            
            freq[{hash1, hash2}]++;
        }
        
        for (auto& p : freq) {
            if (p.second == 1) return true;
        }
        return false;
    }
};