l=[4,5,2,1]
a=[]
b=[]
c=[]
for i in l:
    if i not in a:
        a.append(i)
    elif i in a and i not in b:
        b.append(i)
    elif i in a and i in b:
        c.append(i)
r=[a,b,c]
res=[i for i in r if i]
print(res)
