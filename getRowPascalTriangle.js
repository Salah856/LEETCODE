var getRow = function(rowIndex) {
    let row = []; 
    if(rowIndex < 0 ) return row; 
    row.push(1); 
    
    for(let i = 1; i <= rowIndex; i++){
        
       for(let j = row.length -1 ; j > 0; j--){
           
           row[j] = row[j] + row[j-1];           
       }
        row.push(1);   
    }
    
    return row; 
};
