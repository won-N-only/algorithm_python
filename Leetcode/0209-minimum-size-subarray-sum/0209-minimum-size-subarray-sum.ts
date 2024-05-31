///////슬라이딩윈도우
function minSubArrayLen(target: number, nums: number[]): number {
  let minLength = Infinity;
  let start = 0;
  let end = 0;
  let currentSum = 0;
  while (end < nums.length) {
    currentSum += nums[end];
    end++;

    while (currentSum >= target) {
      minLength = Math.min(minLength, end - start);
      currentSum -= nums[start];
      start++;
    }
    if (minLength == 1) return minLength;
  }

  return minLength == Infinity ? 0 : minLength;
}
