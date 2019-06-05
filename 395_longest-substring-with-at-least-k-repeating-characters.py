class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        l = len(s)
        if l < k:
            return 0
        if l == 1 and k == 1:
            return 1
        res = 0
        count = [0] * 26
        inSub = []
        for i in range(l):
            count[ord(s[i])-ord('a')] += 1
        for i in range(26):
            if count[i] >= k:
                inSub.append(chr(i+ord('a')))
        
        def satisfy(cur: dict) -> bool:
            # print(cur)
            for value in cur.values():
                 if value < k:
                    return False
            return True
        
        for j in range(l-1):
            if s[j] not in inSub:
                continue
            cur = {s[j]:1}
            for m in range(j+1, l):
                if s[m] in inSub:
                    if satisfy(cur):
                        res = max(res, m-j)
                    try:
                        cur[s[m]] += 1
                    except KeyError:
                        cur[s[m]] = 1
                    if m == l-1:
                        if satisfy(cur):
                            res = max(res, m-j+1)
                            return res
                else:
                    if satisfy(cur):
                        res = max(res, m-j)
                    j = m
                    break
        
        return res
