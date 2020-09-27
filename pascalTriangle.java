class Solution {
    public List<List<Integer>> generate(int numRows) {
        
        List<List<Integer>> tr = new ArrayList<>();
        
        if (numRows == 0) return tr; 
        
        
        List<Integer> fr = new ArrayList<>(); 
        
        fr.add(1); 
        
        tr.add(fr);
        
        for(int i =1; i< numRows; i++){
            
            List<Integer> prev = tr.get(i-1); 
            
            List<Integer> row = new ArrayList<>(); 
            
            row.add(1); 
            
            for(int j=1; j<i; j++){
                row.add(prev.get(j-1) + prev.get(j));
                
            }
            
            row.add(1); 
            
            tr.add(row); 
            
        }
        
        
        return tr; 
    }
}
