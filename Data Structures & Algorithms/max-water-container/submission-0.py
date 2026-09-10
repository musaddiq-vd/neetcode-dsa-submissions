class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        l, r = 0, len(heights) -1

        while l < r:
            min_h = min(heights[l], heights[r])
            w = r - l
            current_water = min_h * w

            max_water = max(max_water, current_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water