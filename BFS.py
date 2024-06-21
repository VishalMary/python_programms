def bfs(d,x):
    q.append(x)
    while(q):
        n=q.pop(0)
        if n not in v:
            v.append(n)
            for i in d[n]:
                if i not in q and i not in v:
                    q.append(i)
    return v
d={5:[7,3],7:[5,4],4:[7],3:[5,8],8:[3,2],2:[8]}
q=[]
v=[]
print(bfs(d,5))