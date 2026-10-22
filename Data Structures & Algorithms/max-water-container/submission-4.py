class Solution:

  def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0

    while l < r:
      # 1. Calculate area: width (r - l) multiplied by the shorter height
      area = min(height[l], height[r]) * (r - l)
      res = max(res, area)

      # 2. Move the pointer of the shorter line inward
      if height[l] < height[r]:
        l += 1
      else:
        r -= 1

    return res