class Solution {
public:
    int search(vector<int>& A, int target) {
        int start = 0, end = A.size() - 1; 

        while (start <= end) { 
            int mid = start + (end - start) / 2; 
            
            if (A[mid] == target) { 
                return mid;
            }
            
            
            if (A[start] <= A[mid]) { 
                if (A[start] <= target && target <= A[mid]) {
                    end = mid - 1; 
                } else {
                    start = mid + 1; 
                }
            } 
            
            else { 
                
                if (A[mid] <= target && target <= A[end]) {
                    start = mid + 1; 
                } else {
                    end = mid - 1; 
                }
            }
        } 
        return -1; 
    }
};