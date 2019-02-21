class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        
        if numRows == 1 or numRows > len(s):
            return s
        
        rows= [''] * numRows
        
        for i in range (0, len(s)):
            quo = (i // (numRows-1)) % 2
            rem = i % (numRows - 1)
            if quo:
                rowId = numRows - 1 - rem
            else:
                rowId = rem
            
            rows[rowId] += s[i]
        
        ret = rows[0];
        
        for j in range(1, numRows):
            ret = ret + rows[j];
        
        return ret
