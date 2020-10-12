var minSteps = function(n) {
    if (n <= 1) return 0;
    return rc(n) + 1 // +1 because rc() is called with "c = 1", after the first copy 
};

function rc (n, a = 1, c = 1) { // n = target length, a = current length, c = copied length
    if (a === n) return 0; // found it
    if (a > n) return Infinity; // `A` is too long
    if (a === c) return 1 + rc(n, a + c, c);  // already copied, cannot copy again, can only paste "a + c" means appened copied content
    return 1 + Math.min(rc(n, a, a), rc(n, a + c, c)); // compare copy and paste
}
