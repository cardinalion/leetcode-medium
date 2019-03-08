class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0.0) return 0.0;
        if (n == 0) return 1.0;
        if (n == -2147483648) return myPow(x, -2147483647)/x;
        double base = x;
        int pow = n;
        if (n < 0){
            base = 1/x;
            pow = -n;
        }       
        double cur = base;
        double sum = 1;
        while(pow > 0){
            if (pow % 2 == 1){
                sum *= cur;
            }
            pow /= 2;
            cur *= cur;
        }
        return sum;
    }
};
