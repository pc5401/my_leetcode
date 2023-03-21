/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const jsMap = new Object();
    for(let i = 0; i < nums.length; i++){
        n = nums[i]
        if(target - n in jsMap){
            return [jsMap[target - n], i]
           };
        jsMap[n] = i
        }
};