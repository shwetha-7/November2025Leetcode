/**
 * @param {string} s
 * @return {number}
 */
var numSub = function(s) {
    let total=0,ans=0,mod=Math.pow(10,9)+7;
    for(let i=0;i<s.length;i++){
        if(s.charAt(i)==='0'){
            ans+=(total*(total+1)/2)%mod;
            total=0
        }else{
            total++;
        }
    }
    ans+=(total*(total+1)/2)%mod;
    return ans

};