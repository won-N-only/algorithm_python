function findKthLargest(nums: number[], k: number): number {
  //1차 풀이 일단 정렬해
  //   nums.sort((a, b) => a - b);
  //   return nums[k - 1];

  //2차 풀이 이분탐색
  /* l,r을 inf로 넣어버리니까 m이 NaN이 됨.. 어짬  
  -10^4 <= nums[i] <= 10^4 이니까 맞춰서 설정함 */
  let [l, r]: number[] = [-(10 ** 4) - 1, 10 ** 4 + 1];

  const getCount = (m: number) => {
    let count: number = 0;
    for (const n of nums) {
      if (n >= m) count++;
    }
    return count;
  };

  while (l < r) {
    const m: number = Math.round((r + l) / 2);
    if (getCount(m) >= k) l = m;
    else r = m - 1;
  }

  return l;
}
