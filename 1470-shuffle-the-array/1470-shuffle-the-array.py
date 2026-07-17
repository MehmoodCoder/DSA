# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         i = 0
#         p1 = 0
#         p2 = n
#         num = []

#         while i < n:
#             num.append(nums[p1])
#             num.append(nums[p2])
#             p1 += 1
#             p2 += 1
#             i += 1

#         return num
        

#  Bset Approach


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num = []
        for i in range(n):
            num.append(nums[i])
            num.append(nums[i + n])
        return num