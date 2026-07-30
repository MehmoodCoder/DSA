class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = set("AEIOUaeiou")
        s_list = list(s)


        while l < r:
            if s_list[l] in vowels and s_list[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif s_list[l] in vowels:
                r -= 1
            else:
                l += 1
        s = "".join(s_list)
        return s