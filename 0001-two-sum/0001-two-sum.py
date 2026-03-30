class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return [] 