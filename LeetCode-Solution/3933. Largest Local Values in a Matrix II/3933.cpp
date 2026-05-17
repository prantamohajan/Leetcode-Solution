class Solution {
public:
    int countLocalMaximums(vector<vector<int>>& a) {
        int n = a.size(), m = a[0].size();
        int max_k = max(n, m);
        int logMax = 0;
        while ((1 << logMax) <= max_k) logMax++;
        
        vector<vector<vector<int>>> st(n, vector<vector<int>>(m, vector<int>(logMax + 1)));
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                st[i][j][0] = a[i][j];
            }
            for (int k = 1; k <= logMax; k++) {
                for (int j = 0; j + (1 << k) <= m; j++) {
                    st[i][j][k] = max(st[i][j][k - 1], st[i][j + (1 << (k - 1))][k - 1]);
                }
            }
        }

        auto queryRowMax = [&](int r, int c1, int c2) {
            if (c1 > c2) return 0;
            int len = c2 - c1 + 1;
            int k = 31 - __builtin_clz(len);
            return max(st[r][c1][k], st[r][c2 - (1 << k) + 1][k]);
        };

        int ans = 0;

        // 2. Process each cell
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int x = a[i][j];
                if (x == 0) continue;

                int r1 = max(0, i - x), r2 = min(n - 1, i + x);
                int c1 = max(0, j - x), c2 = min(m - 1, j + x);

                int maxi = 0;

                for (int r = r1; r <= r2; r++) {
                    // Exclude the exact 4 corners where abs(r - i) == x && abs(c - j) == x
                    if (abs(r - i) == x) {
                        int current_c1 = (j - x >= 0) ? j - x + 1 : 0;
                        int current_c2 = (j + x < m) ? j + x - 1 : m - 1;
                        maxi = max(maxi, queryRowMax(r, current_c1, current_c2));
                    } else {
                        // Fully within the row boundaries, query the entire range [c1, c2]
                        maxi = max(maxi, queryRowMax(r, c1, c2));
                    }
                }

                if (maxi <= x) {
                    ans++;
                }
            }
        }

        return ans;
    }
};