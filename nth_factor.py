x = 12
l=[]
k=1
for i in range(1, x + 1):
    if x % i == 0:
        l.append(i)
l.reverse()
print(l)
print(l[k-1])

