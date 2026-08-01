class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        r = len(s) - 1
        l = 0

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True

        
        