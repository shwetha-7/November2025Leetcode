import java.util.LinkedList;
import java.util.List;

class MinimumOperationstoConvertAllElementstoZero{

    class Solution{
       public int minOperations(int[] nums) {
           int count=0;
           List<Integer> stack=new LinkedList<>();
           stack.add(-1);
           for(int num:nums){
                 while(num<stack.get(stack.size()-1)){
                     stack.remove(stack.size()-1);
                 }
                 if(num>stack.get(stack.size()-1)){
                    count+=num>0?1:0;
                    stack.add(num);

                 }
           }


           return count;
       }
    }
    public static void main(String[] args) {
        
    }
}