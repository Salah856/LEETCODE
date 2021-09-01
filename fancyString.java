class Solution {
    
    public String makeFancyString(String s) {
        
        char[] arr=s.toCharArray();
        
        for(int i = 0; i < arr.length-2; i++)
        {
            if(arr[i] == arr[i+1] && arr[i+1] == arr[i+2])
            {
                arr[i] = '0';
            }
        }
        
        StringBuilder sb = new StringBuilder();
        
        for(int i=0;i<arr.length;i++)
        {
            if(arr[i] != '0') sb.append(arr[i]);
        }
        
        
        return sb.toString();
    
    }
}

