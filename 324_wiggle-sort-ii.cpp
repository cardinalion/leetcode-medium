/* refered to leetcode discussion section
 * firstly, used nth_element to find the top half with an average O(n) time
 * then, put the smaller half in the odds position and the larger the opposite
 * finally, adjust positions where value equals the median
 * O(n) time and O(1) space
 */

// TIP: THINK OF DIFFERENT EXAMPLES TO TEST THE BOUNDARY
// WATCH OUT LOOPS

class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        
        int n = nums.size();
        if (n < 2) return;

        auto midptr = nums.begin() + n / 2;
        nth_element(nums.begin(), midptr, nums.end());
        int mid = *midptr;
        

        int start = 0;
        int end = n%2 ? n : n-1;

        for (int i=1; i<n/2; i+=2) {
            swap(nums[i], nums[end-i]);
        }
        if (n%4 == 3) swap(nums[n/2], nums[n/2+1]);
        if (n%2) end = n-2;
        for (int j=0; j<n; j++) {
            if (nums[j] == mid) {
                if (j%2 == 0) {
                    if (j > start) {
                        swap(nums[j], nums[start]);  
                    }
                    start += 2;
                }
                else {
                    if (j < end) {
                        while (nums[end] == mid && end > 2) {
                            end -= 2;
                        }
                        swap(nums[j], nums[end]);
                        end -= 2;
                    }
                }
            }
        }
        return;  
    }
};
