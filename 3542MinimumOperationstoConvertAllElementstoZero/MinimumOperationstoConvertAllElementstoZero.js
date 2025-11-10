/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    let count=0;
    let stack=[-1];
    nums.forEach(num=>
         {
            while(num<stack[stack.length-1]){
                stack.pop()
            }
            if(num>stack[stack.l-1]){
                count+=num>0?1:0;
                stack.push(num)
            }
         }

    )

    return count

};