class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l, r = 0

        while r < len(nums):
            # pop smallest values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # remove Left val from window
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
            
            r += 1
        return output