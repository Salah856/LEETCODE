class Solution {
    
    int pos = 0;
    
    boolean validate(String[] arr) {
        if (pos == arr.length)
            return false;
        
        //If null node
        if (arr[pos].equals("#")) {
            ++pos;
            return true;
        }
        else {
            ++pos;
            //The nodes immediately following current node must be its left and right children.
            boolean isLeftChildValid = validate(arr), isRightChildValid = validate(arr);
            return isLeftChildValid && isRightChildValid;
        }
    }
    
    public boolean isValidSerialization(String preorder) {
        String[] input = preorder.split(",");
        //Even if the function returned true, the input is invalid if any part of it is unused.
        return validate(input) && pos == input.length;
    }
}
