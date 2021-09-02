var minTimeToType = function(word) {
    
    let s = 'abcdefghijklmnopqrstuvwxyz';
    let count = 0;
    let prev = 0;
    
    for (let i = 0; i < word.length; i++) {
        
        let index = s.indexOf(word[i]);
        let moves = Math.abs(index - prev);
        
        count += Math.min(moves, 26 - moves) + 1;
        prev = index;
    }
    
    return count;
    
};
