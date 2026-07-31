class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for l in range(1, n // 2 + 1):
            
            if n % l == 0:
                sub = s[:l]
                
                if sub * (n // l) == s:
                    return True
                    
        return False