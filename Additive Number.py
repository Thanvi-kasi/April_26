class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        for i in range(1, n):
            for j in range(i + 1, n):
                
                a = num[:i]
                b = num[i:j]
                
                if (a.startswith('0') and len(a) > 1) or (b.startswith('0') and len(b) > 1):
                    continue
                
                x, y = int(a), int(b)
                k = j
                
                while k < n:
                    s = x + y
                    s_str = str(s)
                    
                    if not num.startswith(s_str, k):
                        break
                    
                    k += len(s_str)
                    x, y = y, s
                
                if k == n:
                    return True
        
        return False
