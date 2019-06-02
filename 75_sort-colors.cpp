class Solution {
public:
    void sortColors(vector<int>& nums) {
        
        int red = 0, cur = 0, blue = nums.size()-1;
        
        while (cur <= blue){
            if (nums[cur] == 0) swap(nums[cur++], nums[red++]);
            else if (nums[cur] == 2) swap(nums[cur], nums[blue--]);
            else cur++;    
        }   
    }
};
