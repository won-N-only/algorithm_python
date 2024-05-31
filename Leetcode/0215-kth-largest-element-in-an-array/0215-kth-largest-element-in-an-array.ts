function findKthLargest(nums: number[], k: number): number {
  //   let pivot: number = 0; //인덱스로 가져가
  //   let temp: number[] = [];

  //   pivot = nums[pivot];
  //   temp.push(nums.pop() ?? 0);
  //   for (let i: number = 0; i < nums.length; i++) {
  //     if (pivot < nums[i]) temp.push(nums[i]);
  //     if (pivot >= nums[i]) temp.unshift(nums[i]);
  //   }

  //   return 3;
  nums.sort((a, b) => b-a);
  return nums[k - 1];
}