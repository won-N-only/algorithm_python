//스택으로 짜거나 combination쓰면 더 좋을것같음
function maximumTripletValue(nums: number[]): number {
  let ans: number = 0;

  //초기값 설정
  ans = (nums[0] - nums[1]) * nums[2];

  //3중 for문 돌려서 완탐
  for (let i: number = 0; i < nums.length; i++) {
    for (let j: number = i + 1; j < nums.length; j++) {
      if (nums[i] - nums[j] <= 0) continue; //음수 나오거나 second가 이전보다 작으면 건너뛰기

      for (let k: number = j + 1; k < nums.length; k++) {
        if (ans < (nums[i] - nums[j]) * nums[k]) {
          ans = (nums[i] - nums[j]) * nums[k];
        }
      }
    }
  }
  if (ans > 0) return ans;

  return 0;
}
