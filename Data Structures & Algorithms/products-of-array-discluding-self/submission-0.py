class Solution:

  def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Create a result array filled with 1s
    res = [1] * len(nums)

    # 1. Left Pass: One single straight loop (O(n))
    prefix = 1
    for i in range(len(nums)):
      res[i] = prefix
      prefix *= nums[i]

    # 2. Right Pass: Another single straight loop (O(n))
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
      res[i] *= postfix
      postfix *= nums[i]

    return res
