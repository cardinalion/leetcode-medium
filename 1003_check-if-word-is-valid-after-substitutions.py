class Solution:
    def isValid(self, S: str) -> bool:
        
        l = len(S)
        
        if l%3 != 0 or S[0] != 'a' or S[-1] != 'c':
            return False
        
        incomplete= [1]
        li = 1
        
        for i in range(1, l):
            if li == 0:
                if S[i] != 'a':
                    return False
                else:
                    incomplete.append(1)
                    li += 1
            elif incomplete[-1] == 1:
                if S[i] == 'b':
                    incomplete[-1] = 2
                elif S[i] == 'a':
                    incomplete.append(1)
                    li += 1
                else:
                    return False
            else:
                if S[i] == 'c':
                    incomplete.pop()
                    li -= 1
                elif S[i] == 'a':
                    incomplete.append(1)
                    li += 1
                else:
                    return False
        
        if li == 0:
            return True
        return False
