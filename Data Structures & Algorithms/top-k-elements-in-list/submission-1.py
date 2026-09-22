class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in freq.items():
            buckets[c].append(n)

        result = []
        for c in range(len(buckets) - 1, 0, -1):
            for n in buckets[c]:
                result.append(n)
                if len(result) == k:
                    return result
        return result