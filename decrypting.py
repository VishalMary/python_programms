str=input()
k=int(input())
c=k%26
d=''
for i in str:
    if((ord(i)-c)>=97):
        d=d+chr(ord(i)-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)
#a="khoor"
#k=3
#output="hello"
