function isArraySpecial(nums: number[]): boolean {
  let stack: number[] = [];
  if (nums.length == 1) return true;

  for (let i: number = 0; i < nums.length-1; i++) {
    if (!((nums[i] + nums[i + 1]) % 2)) return false;
  }

  return true;
}
