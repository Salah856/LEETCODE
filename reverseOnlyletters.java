class Solution {
    public String reverseOnlyLetters(String S) {
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<S.length();i++)
        {
            char present = S.charAt(i);
            
            if( Character.isLetter(present))
                stack.push(present);
        }
        
        String result = "";
        int count=0;
        while(count<S.length())
        {
            if(Character.isLetter(S.charAt(count)))
            {
                result = result + stack.pop();
                count++;
            }
            else
            {
                result = result+ S.charAt(count);
                count++;
            }        
        }
        
        System.out.println(result);
        return result;
    }
}
