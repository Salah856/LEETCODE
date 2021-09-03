var makeEqual = function(words) {
    
    let d = {};
    let n = words.length;
    
    w = words.join('');
    
    for(let c of w) {
        d[c] = ++d[c] || 1;
    }
    
    for(let key in d) {
        if(d[key] % n) return false;
    }
    
    return true;

};
