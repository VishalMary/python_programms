def allpaths(d,x,cost,l):
    l.append(x)
    if x==2:
        print(l,cost)
        l.pop()
        return
    for (i,c) in d[x]:
        if(i not in l):
            allpaths(d,i,cost+c,l,)
    l.pop()
def costsum(d,x,cost,l,c1):
    l.append(x)
    if x==2:
        c1=c1+cost
        l.pop()
        return c1
    for (i,c) in d[x]:
        if(i not in l):
            c1=costsum(d,i,cost+c,l,c1)
    l.pop()
    return c1
def mincost(d,x,cost,l,b):
    l.append(x)
    if x==2:
        b.append(cost)
        l.pop()
        return
    for (i,c) in d[x]:
        if(i not in l):
            mincost(d,i,cost+c,l,b)
    l.pop()
    return b
def minpath(d,x,cost,l,m,m_path):
    l.append(x)
    if x==2:
        if cost<m:
            m=cost
            m_path=l.copy()
        l.pop()
        return m,m_path
    for (i,c) in d[x]:
        if(i not in l):
            m,m_path=minpath(d,i,cost+c,l,m,m_path)
    l.pop()
    return m,m_path
def allpaths(d,x,cost,l):
    l.append(x)
    if x==2:
        print(l,cost)
        l.pop()
        return
    for (i,c) in d[x]:
        if(i not in l):
            allpaths(d,i,cost+c,l,)
    l.pop()
d={5:[(7,2),(3,3)],7:[(5,2),(4,3),(3,1)],4:[(7,3),(8,3),(2,2)],8:[(3,4),(4,3),(2,1)],3:[(5,3),(7,1),(8,4)],2:[(4,2),(8,1)]}
l=[]
b=[]
allpaths(d,5,0,l)
t=mincost(d,5,0,l,b)
print("Mincost=",min(t)) 
print(minpath(d,5,0,l,999999,[]))
print(costsum(d,5,0,l,0))