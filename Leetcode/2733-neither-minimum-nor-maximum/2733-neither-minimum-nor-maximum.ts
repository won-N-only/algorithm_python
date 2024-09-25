function findNonMinOrMax(nums: number[]): number {
  if (nums.length == 2) return -1;
  let ans: number = 0;
  nums.sort((a, b) => b - a);
  //두번 pop해서 ans 바로 return
  nums.pop();
  ans = nums.pop() ?? -1;
  return ans;
}
