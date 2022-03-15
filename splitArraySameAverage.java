class Solution {

	public boolean splitArraySameAverage(int[] nums) {
			int halflen = nums.length / 2 + 1;
		HashSet<Integer>[] al = new HashSet[halflen];
		for (int i = 0; i < halflen; i++)
			al[i] = new HashSet<Integer>();
		al[0].add(0);
		int sum = 0;
		for (int num : nums) {
			sum = sum + num;
			for (int j = halflen - 2; j >= 0; j--) {
				HashSet<Integer> elements = al[j];
				for (int element : elements) {
					al[j + 1].add(element + num);
				}
			}
		}
		for (int i = 1; i < halflen; i++) {
		    
            // A=So/n this is the formula we have used down 
            int val1=(sum * i) / nums.length;
		   // we are checking to avoid decimal number truncation  
            if (((sum * i) % nums.length)==0 &&al[i].contains(val1))
					return true;
			
		}

		return false;

	}
}
