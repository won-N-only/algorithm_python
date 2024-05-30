/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const num2idx = {};

    for (let idx =0; idx<nums.length; idx++){
        const num=nums[idx];
        const ans = target - num;
        if (ans in num2idx){
            return [num2idx[ans], idx];}
        num2idx[num]= idx;
        }
    
};