class Solution {
public:
    int myAtoi(string str) {
        int l = str.size();
        if (l == 0) return 0;
        int i = 0;
        for (;i < l && isspace(str[i]); i++) ;
        if (i == l || !(isdigit(str[i]) || str[i] == '+' || str[i] == '-')) return 0;
        
        long ret = 0;
        bool minus = false;
        long max = pow(2, 31);
        
        if (str[i] =='-' or  str[i] == '+'){
            if (i == l-1 || !isdigit(str[i+1])) return 0;
            if (str[i] == '-') minus = true;
            i++;
        }
        for (; i < l; i++){
            if (isdigit(str[i])){
                ret = ret*10 + str[i]-'0';
                if (ret >= max && minus == false) return max-1;
                if (ret > max && minus == true) return -max;  
            }
            else break;
        }
        if (minus == true) return -ret;
        return ret;
    }
};
