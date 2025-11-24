/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    let ans=[],val=0;
    for(let i=0;i<nums.length;i++){
        val=(val*2+nums[i])%5;
        ans.push(val===0)
    }

    return ans
};