class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows > s.size()) return s;
        
        vector<string> rows(numRows);
        
        for (int i = 0; i < s.size(); i++){
            int quo = (i / (numRows - 1)) % 2;
            int rem = i % (numRows - 1);
            int rowId = quo ? (numRows - 1 - rem) : rem;
            
            rows[rowId] += s[i];
        }
        
        string ret = rows[0];
        
        for (int j = 1; j < numRows; j++){
            ret = ret + rows[j];
        }
        
        return ret;
    }
};
