l=[14,16,20,22]
def isprime(j):
    for i in range(2, j//2+1):
        if j%i==0:
            return 0
    return j
newl=[]
m=0
for i in range(len(l)-1):
    for j in range(l[i],l[i+1]):
        m=max(isprime(j),m)
    newl.append(m)
print(newl)
print(sum(newl))