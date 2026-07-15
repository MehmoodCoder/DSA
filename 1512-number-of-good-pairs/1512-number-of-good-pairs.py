# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         i = 0
#         counter = 0
        
#         while i < len(nums):
#             j = i + 1 
#             while j < len(nums):
#                 if nums[i] == nums[j]:
#                     counter += 1
#                 j += 1
#             i += 1
            
#         return counter


# 2 

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count_map = {}
        good_pairs = 0
        
        for num in nums:
            if num in count_map:
                good_pairs += count_map[num]
                count_map[num] += 1
            else:
                count_map[num] = 1
                
        return good_pairs
