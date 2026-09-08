class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) +1 )]

        #index = occurence
        for key, value in count.items():
            buckets[value].append(key)

        result = []
        for freq in range(len(buckets)-1 , -1, -1):
            for num in buckets[freq]:
                result.append(num)
                
                if len(result) == k:
                    return result
        