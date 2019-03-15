class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        
        possible = [A[0], B[0]]
        
        minA, minB, minAB, minBA = 0, 0, 0, 0
        l = len(A)
        for i in range(l):
            if minA != -1:
                if A[i] != A[0]:
                    if B[i] != A[0]:
                        minA = -1
                    else:
                        minA += 1
                if B[i] != A[0]:
                    if A[i] != A[0]:
                        minAB = -1
                    else:
                        minAB += 1
            if minB != -1:
                if B[i] != B[0]:
                    if A[i] != B[0]:
                        minB = -1
                    else:
                        minB += 1
                if A[i] != B[0]:
                    if B[i] != B[0]:
                        minBA = -1
                    else:
                        minBA += 1
                
        if minA == -1 and minB == -1:
            return -1
        if minA == -1:
            return min(minB, minBA)
        if minB == -1:
            return min(minA, minAB)
        return min(minA, minB,minAB, minBA)
