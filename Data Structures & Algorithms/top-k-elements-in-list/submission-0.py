class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        result = []
        for num in nums:
            count[num] += 1
        test = list(count.items())
        test.sort(key = lambda x:-x[1])
        test = test[0:k]
        print(test)
        for pair in test:
            result.append(pair[0])
        print(result)
        # for k,v in count.items():
        #     print(v)
        return result