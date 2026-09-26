class Solution {
public:
    int lengthOfLastWord(string s) {
        int siz = s.size();
        int kount = 0;
        int i = siz - 1;
        
        // Skip trailing spaces from the end
        while (i >= 0 && s[i] == ' ')
            i--;
        
        // Count characters until a space is encountered or the beginning of the string is reached
        while (i >= 0 && s[i] != ' ') {
            kount++;
            i--;
        }
        
        return kount;
    }
};

