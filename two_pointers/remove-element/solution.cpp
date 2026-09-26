class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int z = 0;
        int i = 0;
        while(i< nums.size()){
            if (nums[i] != val){
                nums[z] = nums[i];
                z++;
            } i++;
        } return z;
    }
};
