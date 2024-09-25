function maxAscendingSum(nums: number[]): number {
  // minSubArrayLen()
  let max_val: number = -1;
  let sum_val: number = 0;

  for (let i: number = 0; i < nums.length; i++) {
    sum_val = nums[i];
    for (let j: number = i + 1; j < nums.length; j++) {
      if (nums[j] > nums[j - 1]) sum_val += nums[j];
      else break;
    }
    max_val = Math.max(max_val, sum_val);
  }
  return max_val;
}