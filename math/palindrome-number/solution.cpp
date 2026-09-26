class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
      
        long long pal = 0;
        int ori = x;
        while (x != 0) {
            int r = x % 10;
            x = x / 10;
            pal = pal * 10 + r;
        }
        if (pal == ori) {
            return true;
        }
        return false;
    }
};

