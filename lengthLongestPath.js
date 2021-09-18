var lengthLongestPath = function(input) {
    
    if(!input) {
    
        return 0;
    }
    
    let max = 0;
    const dirs = input.split('\n');
    const result = [];
        
    let curr = 0;
    let prev = -1;
    
    for(let i = 0; i < dirs.length; i++) {
        curr = dirs[i].lastIndexOf('\t');
        
        while(curr <= prev) {
            result.pop();
            prev--;
        }
        
        result.push(dirs[i].slice(curr+1));
        
        if(dirs[i].includes('.')) {
            //console.log(result);
            max = Math.max(max, result.join('/').length);
        }
        
        prev = curr;
    }
    
    return max;
};

