class Solution {
   public boolean findRotation(int[][] mat, int[][] target) {

     for(int i=0;i<4;i++){
       if(istrue(mat,target)){
            return true;
        }
        reverse(mat);
    }
    return false;
    
}

public void transpose(int[][] mat)
    {
        int n=mat.length;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                //swap 
                int temp=mat[i][j];
                mat[i][j]=mat[j][i];
                mat[j][i]=temp;
            }
        }
    }
    
    public void reverse(int[][] mat)
    {
        transpose(mat);
        int start=0;
        int end=mat.length-1;
        while(start<=end)
        {
            for(int row=0; row<mat.length ;row++)
            {
                int temp=mat[row][start];
                mat[row][start]=mat[row][end];
                mat[row][end]=temp;
            }
            start++;
            end--;
        }
        
    }
    
    public Boolean istrue(int[][]mat ,int[][] target)
    {
        int n=mat.length;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(mat[i][j]!=target[i][j])
                {
                    return false;
                }
            }
       }
        return true;
    }
 
}

