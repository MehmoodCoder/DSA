class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        return True
        

# I want to solve this problem like this


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         i = 0
#         while len(s) == len(t) and i < len(s):
#             if s[i] in t:
#                 pass
#             else:
#                 return False
#             i += 1
#         return True
        