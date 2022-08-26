# worst solution O(nˆ2)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]


# two pointer solution 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers) - 1
        curr_sum = 0
        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum == target:
                return [start + 1, end + 1]
            elif curr_sum < target:
                start += 1
            else:
                end -= 1
                
        return [start + 1, end]