class Solution {
    public void reorderList(ListNode head) {
        if(head==null)
            return;
        ArrayList<ListNode> a=new ArrayList<ListNode>();
        ListNode temp=head;
        while(temp!=null)
        {
            a.add(temp);
            temp=temp.next;
        }
        temp=head;
        ListNode nex=head.next;
        int n=a.size();
        if(n%2==0){
        for(int i=n-1;i>=n/2;i--)
        {
            temp.next=a.get(i);
            a.get(i).next=nex;
            temp=nex;
            nex=nex.next;
        }
        temp.next=null;
    }
    if(n%2!=0){
        for(int i=n-1;i>=(n/2)+1;i--)
        {
            temp.next=a.get(i);
            a.get(i).next=nex;
            temp=nex;
            nex=nex.next;
        }
        temp.next=null;
    }
    }
}
