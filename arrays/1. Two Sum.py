#   Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


#   Using Hash Map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saw = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in saw:
                return [i, saw[diff]]
            saw[nums[i]] = i


#   Using enumerate() Pythonic way

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saw = {}

        for index, value in enumerate(nums):
            if target - value in saw:
                return [saw[target - value], index]
            saw[value] = index