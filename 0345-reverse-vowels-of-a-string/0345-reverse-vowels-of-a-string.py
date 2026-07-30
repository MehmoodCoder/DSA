# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         l, r = 0, len(s) - 1
#         vowels = set("AEIOUaeiou")
#         s_list = list(s)


#         while l < r:
#             if s_list[l] in vowels and s_list[r] in vowels:
#                 s_list[l], s_list[r] = s_list[r], s_list[l]
#                 l += 1
#                 r -= 1
#             elif s_list[l] in vowels:
#                 r -= 1
#             else:
#                 l += 1
#         
#         return "".join(s_list)


# Accourding to AI


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        l, r = 0, len(s) - 1
        vowels = set("AEIOUaeiou")
        
        while l < r:
            while l < r and s_list[l] not in vowels:
                l += 1
                
            while l < r and s_list[r] not in vowels:
                r -= 1
                
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
            
        return "".join(s_list)