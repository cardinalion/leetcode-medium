class Solution(object):
    def groupAnagrams(self, strs):
        
        l = len(strs)
        if l == 0:
            return []
        if l == 1:
            return [strs]
        chars =  [[]]
        ret = []
        
        for i in range(l):
            char = [0] * 26
            for j in strs[i]:
                char[ord(j)-ord('a')] += 1
            try:
                ind = chars.index(char)
                ret[ind-1].append(strs[i])
            except:
                chars.append(char)
                ret.append([strs[i]])
        return ret
