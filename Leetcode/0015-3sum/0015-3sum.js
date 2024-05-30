/**
 * @param {number[]} nums
 * @return {number[][]}
 */

const sum = (...arr) => arr.reduce((acc, cur) => acc + cur, 0);

var threeSum = function (nums) {
  nums.sort((a, b) => a - b);
  let result = [];
  let i = 0;

  for (i; i < nums.length - 2; i++) {
    let l = i + 1,
      r = nums.length - 1;

    if (i > 0 && nums[i] == nums[i - 1]) continue;
    while (l < r) {
      let summ = sum(nums[i], nums[l], nums[r]);
      if (summ == 0) {
        result.push([nums[i], nums[l], nums[r]]);

        while (l < r && nums[l] == nums[l + 1]) l++;
        while (l < r && nums[r] == nums[r - 1]) r--;

        l++;
        r--;
      } else if (summ < 0) l++;
      else r--;
    }
    if (nums[i] >= 0) return result;
  }
  return result;
};

