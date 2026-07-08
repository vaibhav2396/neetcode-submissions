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
        for j in range(len(freq)-1, 0, -1):
            for value in freq[j]:
                result.append(value)
                i += 1
                if i == k:
                    return result

    
        return result