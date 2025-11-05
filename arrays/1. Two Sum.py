#   Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


#   HashMap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i in range(len(nums)):

            if target - nums[i] in hashMap:
                return [i, hashMap[target - nums[i]]]
            else:
                hashMap[nums[i]] = i


#   Using enumerate() Pythonic way

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saw = {}

        for index, value in enumerate(nums):
            if target - value in saw:
                return [saw[target - value], index]
            saw[value] = index

#   Two Pointer Approach (Requires Sorted Array)
#   Note: This approach won't return original indices if the array is not sorted.
#   We cannot use this approach directly for the original problem without additional steps.