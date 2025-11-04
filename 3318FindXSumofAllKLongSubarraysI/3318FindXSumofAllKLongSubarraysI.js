/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findXSum = function(nums, k, x) {
    const xsum = (sub_array,x)=>{
        const hash_map=new Map()
        sub_array.forEach(item=>

            hash_map.set(item,(hash_map.get(item) ||0) +1)
        )
        let res_arr=[]
        for(let [key,value] of hash_map){
            res_arr.push([key,value])
        }
        res_arr=res_arr.toSorted((a,b)=>a[0]-b[0]);
        res_arr=res_arr.toSorted((a,b)=>a[1]-b[1]);
        if(res_arr.length<x){
            let total=0;
            res_arr.forEach(item=>

                total+=item[0]*item[1]
            )
            return total
        }
        let total=0;
        while(x!==0){
            let curr=res_arr.pop();
            total+=curr[0]*curr[1]
            x-=1
        }
        return total;
    }
    
    let n=nums.length;
    let res=[]
    for(let i=0;i<n-k+1;i++){

        let temp=xsum(nums.slice(i,i+k),x);
        res.push(temp)

    }
    return res
       
};

findXSum([1,1,2,2,3,4,2,3],6,2)
