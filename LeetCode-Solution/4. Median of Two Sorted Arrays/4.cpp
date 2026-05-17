class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            return findMedianSortedArrays(nums2, nums1); 
        }
        
        int m = nums1.size();
        int n = nums2.size();
        int left = 0, right = m;
        
        while (left <= right) {
            int partition1 = (left + right) / 2;
            int partition2 = (m + n + 1) / 2 - partition1;
            
            // Get left and right values (handle boundaries)
            int left1 = (partition1 == 0) ? INT_MIN : nums1[partition1 - 1];
            int right1 = (partition1 == m) ? INT_MAX : nums1[partition1];
            
            int left2 = (partition2 == 0) ? INT_MIN : nums2[partition2 - 1];
            int right2 = (partition2 == n) ? INT_MAX : nums2[partition2];
            
            // Found correct partition
            if (left1 <= right2 && left2 <= right1) {
                // Odd total length
                if ((m + n) % 2 == 1) {
                    return max(left1, left2);
                }
                // Even total length
                return (max(left1, left2) + min(right1, right2)) / 2.0;
            }
            // Too many elements in left part of nums1
            else if (left1 > right2) {
                right = partition1 - 1;
            }
            // Too few elements in left part of nums1
            else {
                left = partition1 + 1;
            }
        }
        
        return 0.0; 
    }
};