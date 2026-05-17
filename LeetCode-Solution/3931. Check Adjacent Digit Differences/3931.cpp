class Solution {
public:
    bool isAdjacentDiffAtMostTwo(string s) {
        if (s.length() < 2) {
            return true;
        }
        
        for (int i = 0; i < s.length() - 1; i++) {
            int d1 = s[i] - '0';
            int d2 = s[i + 1] - '0';
            if (abs(d1 - d2) > 2) {
                return false;
            }
        }
        return true;
    }
};