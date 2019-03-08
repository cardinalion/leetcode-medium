class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        pos0 = []
        pos1 = []
        count0 = 0
        count1 = 0
        
        if A[0] == 1:
            pos0.append(0)
            count1 = 1
        else:
            count0 = 1
        
        l = len(A)
        
        for i in range(1, l):
            if A[i] == 1:
                if count1 > 0:
                    count1 += 1
                else:
                    pos0.append(count0)
                    count0, count1 = 0, 1 
            else:
                if count0 > 0:
                    count0 += 1
                else:
                    pos1.append(count1)
                    count0, count1 = 1, 0
        if count0 > 0:
            pos0.append(count0)
        else:
            pos1.append(count1)
            pos0.append(0)
        
        ret = 0
        l1 = len(pos1)
        if l1 == 0:
            return min(K, l)
        
        for i in range(l1):
            sum0 = 0
            sum = pos1[i]
            for j in range(i+1, l1):
                sum0 += pos0[j]
                if sum0 == K:
                    ret = max(ret, sum+pos1[j]+sum0)
                    break
                if sum0 < K:
                    sum += pos1[j]
                    if j == l1-1:
                        sum0 += pos0[i] + pos0[-1]
                        if sum0 >= K:
                            ret = max(ret, sum+K)
                        else:
                            ret = max(ret, sum+sum0)
                else:
                    ret = max(ret, sum+K)
                    break
        ret = max(ret, min(pos1[-1]+K, pos1[-1]+pos0[-1]+pos0[-2]))
        
        return ret
