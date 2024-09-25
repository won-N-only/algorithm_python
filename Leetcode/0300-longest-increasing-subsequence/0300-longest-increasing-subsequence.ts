let nums: number[] = [10, 9, 2, 5, 3, 7, 101, 18];
function lengthOfLIS(nums: number[]): number {
  const dp: number[] = [];

  for (let num of nums) {
    let left = 0,
      right = dp.length;

    while (left < right) {
      let mid = Math.floor((left + right) / 2);
      if (dp[mid] < num) left = mid + 1;
      else right = mid;
    }

    if (left < dp.length) dp[left] = num;
    else dp.push(num);
  }
  console.log(dp);

  return dp.length;
}