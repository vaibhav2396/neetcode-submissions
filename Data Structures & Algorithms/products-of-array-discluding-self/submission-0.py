class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        result = []
        # if count[0] > 1:
        #     return result
        for num in nums:
            product = 1
            for key,value in count.items():
                if num == key:
                    if value > 1:
                        product *= key ** (value-1)
                else:
                    product *= key ** value
            result.append(product)
        return result