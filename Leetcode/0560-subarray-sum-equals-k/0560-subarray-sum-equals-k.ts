function subarraySum(nums: number[], k: number): number {
  const n = nums.length;
  const dp: number[] = new Array(n + 1);
  dp[0] = 0;

  //dp배열 만듦
  for (let i = 0; i < n; i++) {
    dp[i + 1] = dp[i] + nums[i];
  }

  let cnt: number = 0;

  //돌면서 부분합있으면 ++, 초과하면 브레이크
  for (let s: number = 0; s < n; s++)
    for (let e: number = s + 1; e <= n; e++) {
      if (dp[e] - dp[s] == k) cnt++;
    }

  return cnt;
}