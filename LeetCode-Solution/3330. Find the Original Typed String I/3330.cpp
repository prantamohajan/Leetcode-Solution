#include <string>
#include <iostream>
class Solution {
public:
    int possibleStringCount(std::string word) {
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(NULL);
        
        int count = 1;
        int n = word.length();
        if (n <= 1) return count; 

        for (int i = 1; i < n; ++i) {
            if (word[i] == word[i - 1]) {
                count++;
            }
        }
        
        return count;
    }
};