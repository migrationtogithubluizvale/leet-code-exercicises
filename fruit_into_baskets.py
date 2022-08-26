class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        end = 0
        max_len = 0
        d = {}
        while end < len(fruits):
            d[fruits[end]] = end
            
            if len(d) >= 3:
                min_value = min(d.values())
                del d[fruits[min_value]]
                start = min_value + 1
                
            max_len = max(max_len, end - start + 1)
            end += 1
            
        return max_len