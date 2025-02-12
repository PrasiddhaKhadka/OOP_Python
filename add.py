class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            # print(i)s
            for j in range(i, len(nums)):
                # print(j)
                if nums[i] + nums[j] == target:
                    # print(i, j)
                    # print(nums[i], nums[j])
                    return [i, j]
            
    
obj = Solution()
obj.twoSum([2,7,11,15], 18)


# list = [1,2,3,4,5,6]
# print(len(list))