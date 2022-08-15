class Solution:
    # optmal solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # value:index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash_map:
                return [hash_map[diff], i]
            
            hash_map[n] = i
            
        return