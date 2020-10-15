class Solution {
    public int[] nextLargerNodes(ListNode head) {
        ArrayList<Integer> vals  = new ArrayList(); 
        ListNode cur = head; 
        while(cur!=null){
            vals.add(cur.val); 
            cur = cur.next;    
        }
        
        int[] res = new int[vals.size()]; 
        
        Stack<Integer> st = new Stack(); 
        
        for(int i = 0; i < vals.size(); i++){
            
            while(!st.isEmpty() && vals.get(st.peek()) < vals.get(i)){
                res[st.pop()] = vals.get(i); 
            }
            
            st.push(i); 
            
        }
        
        return res; 
    }
}
