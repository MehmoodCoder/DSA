# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = 0
#         read = 0
#         write = 0

#         while i < len(nums):
#             if nums[i] == 0:
#                 read += 1
#             else:
#                 nums[write] = nums[i]
#                 write += 1
#             i += 1

#         j = write
#         while j < len(nums):
#             nums[j] = 0
#             j += 1


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Optimal Approach Two Pointer Swap


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        read = 0
        write = 0

        while i < len(nums):
            if nums[i] == 0:
                read += 1
            else:
                nums[i], nums[write] = nums[write], nums[i]
                write += 1
            i += 1

