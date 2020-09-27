class Solution:
    def countAndSay(self, n: int) -> str:
        a='1'
        for i in range(n-1):
            k=1
            b=''
            for i in range(1,len(a)):
                if a[i]==a[i-1]:
                    k+=1
                else:
                    b+=str(k)
                    b+=a[i-1]
                    k=1
            if k>0:
                b+=str(k)
                b+=a[-1]
            a=b
        return a
