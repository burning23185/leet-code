class Solution:

    def rob(self, nums: list[int]) -> int:
        """
        dy[n] = max(dy[n-2]+n, dy[n-1])
        prev_prev : n-2
        prev : n-1
        now : n
        """
        prev_prev = 0
        prev = 0

        for n in nums:
            now = max(prev_prev + n, prev)
            prev_prev = prev
            prev = now

        return now