class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0

        for i, jump in enumerate(nums):
            # If the current index is beyond our furthest reachable index, we're stuck
            if i > max_reach:
                return False

            # Update the furthest index reachable from any index seen so far
            max_reach = max(max_reach, i + jump)

            # Early exit once we can reach or pass the final index
            if max_reach >= len(nums) - 1:
                return True

        return True