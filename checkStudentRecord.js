var checkRecord = function (s) {
    
    let a = s.split('');
    let b = 0;

    for (i = 0; i < a.length; i++) {
        if (a[i] === 'A') {
            b++;
        }
    }

    for (i = 0; i < a.length - 2; i++) {
        
        if (a[i] === 'L' && a[i + 1] === 'L' && a[i + 2] === 'L') {
            return false;
        }
    }

    
    return b < 2;

};
