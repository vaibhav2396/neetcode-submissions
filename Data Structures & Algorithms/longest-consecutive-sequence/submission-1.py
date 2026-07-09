class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        (2,20,10,3,4,5)
        numsSet = set(nums)

        start = []

        for num in nums:
            if num - 1 in numsSet:
                continue
            start.append(num)
        
        maxCount = 0
        for num in start:
            count = 1
            current = num
            while True:
                if current + 1 in numsSet:
                    count += 1
                    current += 1
                else:
                    break
            maxCount = max(maxCount,count)
        
        return maxCount

        