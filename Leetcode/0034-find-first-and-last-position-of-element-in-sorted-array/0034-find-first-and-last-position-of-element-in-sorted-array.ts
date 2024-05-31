function searchRange(nums: number[], target: number): number[] {
  let lf: number = 0,
    rt: number = nums.length - 1;
  while (lf <= rt) {
    if (target > nums[lf]) lf += 1;
    if (target < nums[rt]) rt -= 1;
    if (nums[lf] == target && nums[rt] == target) return [lf, rt];
  }
  return [-1, -1];
}