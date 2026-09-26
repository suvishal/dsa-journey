class Solution {
public:
    int numberOfSteps(int num) {
       int op = 0;
        while (num){
            num = num %2 ? num - 1 : num/2;
            op ++;}
        return op;
    }
};
