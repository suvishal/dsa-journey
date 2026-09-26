class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int max = 0; // max count
        int curr = 0; // current count
        int i = 0;

        while (i < nums.size()) {
            int num = nums[i];
            if (num == 1) {
                curr++; // Increment the current count
                if (curr > max) {
                    max = curr; // Update max count if necessary
                }
            } else {
                curr = 0; // Reset the current count if a zero is encountered
            }

            i++;
        }

        return max;
    }
};

