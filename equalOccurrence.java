class Solution {
    public boolean areOccurrencesEqual(String s) {
        
        int[] alph = new int[26];
        int occurance = 0;
        
        for(int i =0; i< s.length(); i++){
            alph[s.charAt(i)-'a']++;
            occurance = Math.max(occurance, alph[s.charAt(i)-'a']);
        }
        
        for(int i = 0; i < 26; i++){
            if(alph[i] != 0 && alph[i] != occurance) return false;
        }
        
        return true;
    }
}
