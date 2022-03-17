class Solution {
    public int consecutiveNumbersSum(int n) {
        int count = 1;
        for(int i = 2; i < n; i++){
            
            if(i % 2 == 0){ // for even number of consecutive numbers
                if((i*i+i)/2 > n){
                    break; //avoid further checking 
                }
                if(n >= (i*i+i)/2 && n % i == i/2){
                    count++; 
                }
            }else{ //for odd
                if(i*(i/2 + 1) > n){
                    break;
                }
                if(n >= i*(i/2 + 1) && n % i == 0){
                    count++;
                }
            }
        }
        return count;
    }
}
