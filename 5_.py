a="MMFMFFMFMFMFFMMFFMMFFMM"
#l=list(a)
count1=0
count2=0
for i in a:
    if i=="M":
        count1+=1
    if i=="F":
        count2+=1
if count1==count2:
    print(0)
elif count1>count2:
    print("M")
else:
    print("F")
    
a="MMFMFFMFMFMFFMMFFMMFFMM"
c=0
for i in a:
    if i=="M":
        c=c+1
    else:
        c=c-1
if c==0:
    print(0)
elif c>0:
    print("M")
else:
    print("F")