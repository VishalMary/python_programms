ip="abcdefghjkl"
n=len(ip)
count=1
m=0
for i in range(len(ip)-1):
    if ord(ip[i])<ord(ip[i+1]):
        count=count+1
        i=i+1
    else:
        if(count>m):
            m=count
        count=1
if(count>m):
    m=count
print(m)
