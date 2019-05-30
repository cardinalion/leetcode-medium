class Solution:
    
    num = {
        '2':['a', 'b', 'c'], 
        '3':['d', 'e', 'f'], 
        '4':['g', 'h', 'i'], 
        '5':['j', 'k', 'l'], 
        '6':['m', 'n', 'o'], 
        '7':['p', 'q', 'r', 's'], 
        '8':['t', 'u', 'v'], 
        '9':['w', 'x', 'y', 'z']
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        # num = ['2':[a, b, c], '3':[d, e, f], '4':[g, h, i], '5':[j, k, l], '6':[m, n, o], '7':[p, q, r, s], '8':[t, u, v], '9':[w, x, y, z]]
        
        l = len(digits)
        if l < 1:
            return []
        ret = self.num[digits[0]]
        for i in range(1, l):
            ret = self.combine(ret, digits[i])
        
        return ret
        
            
    def combine(self, original: List[str], digit: str) -> List[str]:
        ret = []
        for i in self.num[digit]:
            for j in original:
                ret.append(j+i)
        return ret
