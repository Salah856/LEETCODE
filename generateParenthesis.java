class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList(); 
        backtrack(res, "", 0, 0, n); 
        return res; 
    }
    
      public  void backtrack(List<String> res, String current, int open, int close,  int max){
            if(current.length() == max * 2 ){
                res.add(current); 
                return; 
            }     
          if(open < max) backtrack(res, current + "(", open+1, close, max);  
          if(close < open) backtrack(res, current+")" , open , close +1 , max); 
    }
}

