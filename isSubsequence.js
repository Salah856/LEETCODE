var isSubsequence = function(s, t) {
    
    let lastSeen = -1;
    let counter = 0;
    
    for(let i = 0; i < t.length; i++){
      
      if(t[i] === s[counter] && i > lastSeen ){
        lastSeen = i;
        counter++;
      }
    }
    
    return counter === s.length;
};
