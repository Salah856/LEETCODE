var replaceElements = function(arr) {
    let newArr = [];
    newArr[arr.length-1] = -1;
    for (i = arr.length-2; i >= 0; i--) {
        newArr[i] = Math.max(newArr[i+1],arr[i+1]);
    }
    return newArr;
};
