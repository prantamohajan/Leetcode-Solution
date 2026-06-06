#include <iostream>
#include <string>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
private:
    pair<long long, long long> memo[20][2][2][12][12];
    string numStr;

    pair<long long, long long> dp(int idx, bool isTight, bool isLeadingZero, int prevPrevDigit, int prevDigit) {
        if (idx == numStr.length()) {
            return {1, 0}; 
        }

        int pp_idx = prevPrevDigit + 1;
        int p_idx = prevDigit + 1;

        if (memo[idx][isTight][isLeadingZero][pp_idx][p_idx].first != -1) {
            return memo[idx][isTight][isLeadingZero][pp_idx][p_idx];
        }

        int limit = isTight ? (numStr[idx] - '0') : 9;
        long long totalCount = 0;
        long long totalWave = 0;

        for (int d = 0; d <= limit; ++d) {
            bool newTight = isTight && (d == limit);
            bool newLeadingZero = isLeadingZero && (d == 0);

            int newPrevPrev = -1, newPrev = -1;
            long long addWave = 0;

            if (newLeadingZero) {
                newPrevPrev = -1;
                newPrev = -1;
            } else {
                if (isLeadingZero) {
                    newPrevPrev = -1;
                    newPrev = d;
                } else if (prevPrevDigit == -1) {
                    newPrevPrev = prevDigit;
                    newPrev = d;
                } else {
                    newPrevPrev = prevDigit;
                    newPrev = d;
                    if ((prevPrevDigit < prevDigit && prevDigit > d) || 
                        (prevPrevDigit > prevDigit && prevDigit < d)) {
                        addWave = 1;
                    }
                }
            }

            auto [childCount, childWave] = dp(idx + 1, newTight, newLeadingZero, newPrevPrev, newPrev);
            totalCount += childCount;
            totalWave += childWave + addWave * childCount;
        }

        return memo[idx][isTight][isLeadingZero][pp_idx][p_idx] = {totalCount, totalWave};
    }

    long long calculateWaviness(long long limitNum) {
        if (limitNum < 0) return 0;
        numStr = to_string(limitNum);
        memset(memo, -1, sizeof(memo));
        return dp(0, true, true, -1, -1).second;
    }

public:
    long long totalWaviness(long long num1, long long num2) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        return calculateWaviness(num2) - calculateWaviness(num1 - 1);
    }
};