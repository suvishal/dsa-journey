class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = nums[0]; // Initialize candidate with the first element
        int count = 1;
        int i = 1;
        while (i < nums.size()) {
        
            if (nums[i] == candidate) {
                count++;
            } else {
                count--;
                if (count == 0) {
                    candidate = nums[i];
                    count = 1;
                }
            } i++;
        }

        return candidate;
    }
};

