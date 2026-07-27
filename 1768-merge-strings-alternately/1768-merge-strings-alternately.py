# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         merged_str = ""
#         counter = 0

#         if len(word1) == len(word2):
#             for i in range(len(word1)):
#                 merged_str += (word1[i] + word2[i])
#         elif len(word1) > len(word2):
#             for i in range(len(word2)):
#                 counter += 1
#                 merged_str += (word1[i] + word2[i])
#             merged_str += word1[len(word1) - counter:]
#         else:
#             for i in range(len(word1)):
#                 counter += 1
#                 merged_str += (word1[i] + word2[i])
#             merged_str += word2[len(word2) - counter:]
            
#         return merged_str




# Clean code


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged = []
        i = 0
        n1,n2 = len(word1), len(word2)
        
        while n1 > i and n2 > i:
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1

        merged.append(word1[i:])
        merged.append(word2[i:])
        
        return "".join(merged)
