class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        
        int sum = 0;
        int arrSize = 1;
        
        // repeating loop odd number of times.
        
        while (arrSize <= arr.length) {
             
            for (int i = 0; i < arr.length - (arrSize - 1); i++) {

                //Below loop gives us sum of array elements.
                
                for (int j = i; j < i + arrSize; j++) {
                    sum += arr[j];
                }
            }
            arrSize = arrSize + 2;
        }
        return sum;
    }
}
