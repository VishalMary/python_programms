a = "leet**cod*e"
b = []
for i in a:
    if(i!="*"):
        b.append(i)
    else:
        b.pop()
print(''.join(b))
