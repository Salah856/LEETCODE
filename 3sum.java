
class Solution{

        public List<List<Integer>> threeSum(int[] nums) {
                List list = new ArrayList();
                if(nums.length < 3){
                    return list;
                }
                Arrays.sort(nums);
                for(int i = 0;i < nums.length - 2;i++){
                    if(i > 0 && nums[i] == nums[i-1]){
                        continue;
                    }
                    int sum = nums[i];
                    int front = i+1;
                    int end = nums.length -1;
                    while(front < end){
                        if(end < nums.length -1 && nums[end] == nums[end+1]){
                            end--;
                            continue;
                        }
                        if(front>i+1 && nums[front] == nums[front-1]){
                            front++;
                            continue;
                        }
                        if(nums[front] + nums[end] == -sum){
                            ArrayList triplet = new ArrayList();
                            triplet.add(sum);
                            triplet.add(nums[front]);
                            triplet.add(nums[end]);
                            list.add(triplet);
                            end--;
                            front++;
                        }else if(nums[front] + nums[end] > -sum){
                            end--;
                        }else{
                            front++;
                        }
                    }
                }
                return list;
     }
} 




