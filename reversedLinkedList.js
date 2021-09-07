var reverseList = function(head) {
    
  let cur = head;
   let prev = null;
   let tmp;
    
  while( cur != null){
        tmp = cur.next;
        cur.next = prev;
        prev = cur;
        cur = tmp;
    }
    
  return prev;
};
