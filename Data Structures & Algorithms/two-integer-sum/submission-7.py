class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_dict = {}

        for i in range(len(nums)):
            sum_dict[nums[i]] = i
        
        for i in range(len(nums)):
            if(target - nums[i] in sum_dict and sum_dict[target-nums[i]] != i ):
                return [i, sum_dict[target-nums[i]]]