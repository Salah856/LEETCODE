func rotate(nums []int, k int)  {
    k = k % len(nums)
    lastK := len(nums) - k
    
  copy(nums, append(nums[lastK:], nums[:lastK]...))
}
