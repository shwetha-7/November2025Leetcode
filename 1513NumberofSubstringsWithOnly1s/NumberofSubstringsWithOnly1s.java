
public class NumberofSubstringsWithOnly1s {
    private class Solution{
     public int numSub(String s) {
          long ans=0,total=0,mod=1000000007L;
          for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='1'){
                total++;
            }else{
                ans = (ans + ((total * (total + 1)) / 2) % mod) % mod;
                total=0;
            }
          }

         ans = (ans + ((total * (total + 1)) / 2) % mod) % mod; 
          return (int)ans;
      }   
    }
}
