/**
 * @param {number[][]} intervals
 * @return {number}
 */
var intersectionSizeTwo = function(intervals) {
    let ans=0,p1=Number.MIN_VALUE,p2=Number.MIN_VALUE;
    intervals.sort((a,b)=> a[1]>b[1] || (a[1]===b[1] && a[0]>b[0]));
    
    for(let interval of intervals){
        let start=interval[0],end=interval[1];
        if(start<=p1) continue;
        if(start>p2){
            ans+=2;
            p2=end;
            p1=p2-1
        }else{
            ans++;
            p1=p2;
            p2=end
        }
    }

    return ans
};