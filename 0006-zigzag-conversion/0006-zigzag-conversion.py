class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)

            if idx == 0: # 맨 위
                d = 1 # 아래 방향
            elif idx == numRows - 1: # 맨 아래
                d = -1 # 위 방향
            
            idx += d
    
        return ''.join([''.join(_) for _ in rows])

