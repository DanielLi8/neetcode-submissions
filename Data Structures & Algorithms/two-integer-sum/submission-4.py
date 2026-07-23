class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen= {}

        for i in range(len(nums)):
            first_index =target-nums[i]
            if first_index in seen:
                return [seen[first_index],i]
            else:
                seen[nums[i]] = i
    