class Solution 
{
    public boolean backspaceCompare(String S, String T) 
    {
        char Sarr[]=S.toCharArray();
        char Tarr[]=T.toCharArray();
        Stack<Character> stack=new Stack<>();
        for(int i=0;i<Sarr.length;i++)
        {
            if(Sarr[i]!='#')
            {
                stack.push(Sarr[i]);
            }
            else if(Sarr[i]=='#' && !stack.isEmpty())  //for cases such as a##a
            {
                stack.pop();
            }
        }
        String newS="";
        while(!stack.isEmpty())
        {
            newS=stack.pop()+newS;
        }
        
        for(int i=0;i<Tarr.length;i++)
        {
            if(Tarr[i]!='#')
            {
                stack.push(Tarr[i]);
            }
            else if(Tarr[i]=='#' && !stack.isEmpty())
            {
                stack.pop();
            }
        }
        
        String newT="";
        while(!stack.isEmpty())
        {
            newT=stack.pop()+newT;
        }
        
        if(newS.equals(newT))
        {
            return true;
        }
        return false;
        //System.out.println(newS);

        
    }
}
