def findArraySum(a, n, b, m):
    # Write your code here.
    s1 = ""
    s2 = ""
    
    for i in range(n):
        s1 += str(a[i])
    
    s1 = int(s1)
    
    for i in range(m):
        s2 += str(b[i])
    
    s2 = int(s2)
    
    st = str(s1 + s2)
    
    l = len(st)
    z = []
    for i in range(l):
        z.append(int(st[i]))
        
    return z
    
        
