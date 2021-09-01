var numDupDigitsAtMostN = function(n) {
   

   let i = 1, c = 0; 
   
   for(i=1; i <= n; i++){
       
       str = "" + i;  
       arr = str.split(''); 
       set = new Set(arr); 
       
       if (set.size != arr.length)  c++; 
       
   }
    
    return c;  
};
