class Solution:
    def reorganizeString(self, S: str) -> str:
        size = len(S)
        c = Counter(S)
        s = sorted(c.items(), key=lambda x:-x[1])
        if s[0][1]>(size+1)//2:
                return ""
        size1,size2 = (size+1)//2,size//2
        odd = [0]*size1
        even = [0]*size2
        idx1,idx2 = 0,0
        for key,nums in s:
            for j in range(nums):
                if idx1<len(odd):
                    odd[idx1] = key
                    idx1+=1
                else:
                    even[idx2] = key
                    idx2+=1
        ans = []
        idx1,idx2 = 0,0
        while odd or even:
            ans.append(odd.pop(0))
            if even:
                ans.append(even.pop(0))
        return "".join(ans)
            
            
