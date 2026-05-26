class Solution {
public:
    int numberOfSpecialChars(string word) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        
        bool lower[26] = {false};
        bool upper[26] = {false};

        
        for (char c : word) {
            if (c >= 'a' && c <= 'z') {
                lower[c - 'a'] = true; 
            } else if (c >= 'A' && c <= 'Z') {
                upper[c - 'A'] = true; 
            }
        }

        int ans = 0;
        for (int i = 0; i < 26; i++) {
            if (lower[i] && upper[i]) {
                ans++;
            }
        }

        return ans;
    }
};