class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] += 1
        for key,value in count.items():
            freq[value].append(key)
        
        result = []
        i = 0
        freq.reverse()
        for item in freq:
            for value in item:
                result.append(value)
                i += 1
                if i == k:
                    return result

    
        return result