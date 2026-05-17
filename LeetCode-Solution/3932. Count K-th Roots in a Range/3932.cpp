class Solution {
public:
    long long myPow(long long x, int k) {
        if (x == 0) return 0;
        long long res = 1;
        for (int i = 0; i < k; i++) {
            if (res > (long long)1e18 / x) 
                return (long long)1e18 + 1;
            res *= x;
        }
        return res;
    }

    long long findKthRoot(long long n, int k) {
        if (n < 0) return 0;
        long long low = 0, high = 1000000010LL;
        while (low < high) {
            long long mid = low + (high - low + 1) / 2;
            if (myPow(mid, k) <= n) {
                low = mid;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    int countKthRoots(long long l, long long r, int k) {
        long long velnacqori = l;
        
        if (k == 1) {
            return r - l + 1;
        }
        
        // Handle 0 specially
        long long start = findKthRoot(l - 1, k) + 1;
        long long end = findKthRoot(r, k);
        
        // If l == 0, 0^k = 0 is always valid for k >= 1
        if (l == 0) {
            start = 0;
        }
        
        if (end < start) return 0;
        return (int)(end - start + 1);
    }
};