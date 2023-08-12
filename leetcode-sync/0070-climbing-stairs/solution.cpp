class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        
        long long prev1 = 1, prev2 = 2;
        
        for (int i = 3; i <= n; ++i) {
            long long current = prev1 + prev2;
            prev1 = prev2;
            prev2 = current;
        }
        
        return prev2;
    }
};


