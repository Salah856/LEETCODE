class Solution {
	public int findInMountainArray(int target, MountainArray mArr) {
		int s=0;
		int e=mArr.length()-1;
		int p=pivot(mArr,target,s,e);

		if(mArr.get(p)<target){
			return -1;
		}
		if(mArr.get(p)==target){
			return p;
		}

		int ans=search(mArr,target,0,p-1,true);
		if(ans==-1)  
		ans=search(mArr,target,p+1,mArr.length()-1,false);

		return ans;
	}

	int pivot(MountainArray mArr,int target,int s, int e){
		while(s<=e){
			int m=(s+e)/2;
			if(m>0 && mArr.get(m-1)<mArr.get(m) && mArr.get(m+1)<mArr.get(m)){
				return m;
			}else if(mArr.get(m+1)>mArr.get(m)){
				s=m+1;
			}else if(mArr.get(m+1)<mArr.get(m)){
				e=m-1;
			}
		}
		return -1;
	}

	int search(MountainArray mArr,int target,int s, int e,boolean asc){
		while(s<=e){
			int m=(s+e)/2;

			if(mArr.get(m)==target){
				return m;
			}
			if(mArr.get(m)<target){
				if(asc){
					s=m+1;
				} else {
					e=m-1;
				}
			}else {
				if(asc){
					e=m-1;
				} else {
					s=m+1;
				}
			}
		}
		return -1;
	}

}
