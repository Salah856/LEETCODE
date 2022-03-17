class UnionFind(object):
    def __init__(self,size):
        self.arr=[i for i in range(size)]
        self.size=size
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a==b:
            return 0
        self.arr[b]=self.arr[a]
    def find(self,a):
        root=a
        while(self.arr[a]!=a):
            a=self.arr[a]
        while(self.arr[root]!=a):
            b=self.arr[root]
            self.arr[root]=a
            root=b
        return a
    def count(self):
        a={}
        for item in range(self.size):
            a[self.find(item)]=1
        return len(a)
        
class Solution(object):
    def numSimilarGroups(self, strs):
        def check(item,item1):
            count=0
            for i in range(len(item)):
                if item[i]!=item1[i]:
                    count+=1
                if count>2:
                    return 0
            return 1
        graph={}
        for i in range(len(strs)):
            graph[i]=[]
        for i,item in enumerate(strs):
            for j in range(i+1,len(strs)):
                if check(item,strs[j]) :
                        graph[i].append(j)
        uf = UnionFind(len(strs))
        visited={}
        for item in graph:
            for item1 in graph[item]:
                uf.union(item,item1)
        return uf.count()
        
