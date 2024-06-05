a="is2 sentence4 This1 a3"
b=a.split()
s=[0]*len(a)
for i in b:
    s[int(i[-1])-1]=i[:-1]
print(''.join(s))
