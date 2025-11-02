import java.util.LinkedHashMap;
import java.util.Map;

class DeleteNodesFromLinkedListPresentinArray{
    private class ListNode{
        int val;
        ListNode next;
        ListNode(int val){
           this.val=val;
           this.next=null;
 
        }
    }
    
    private class Solution{
    public ListNode modifiedList(int[] nums, ListNode head) {
        Map<Integer,Integer> map=new LinkedHashMap<Integer,Integer>();
        for(int num:nums){
            map.put(num, 1);
        }
        ListNode dummy_head=new ListNode(0);
        ListNode res=dummy_head; 
        ListNode curr=head; 
        while(curr!=null){
                int value = curr.val;
                if(!map.containsKey(value)){
                    dummy_head.next=curr;
                    dummy_head=dummy_head.next;
                }
                ListNode next=curr.next;
                curr.next=null;
                curr=next;
        }

        
        return res.next;

    }
    }
}