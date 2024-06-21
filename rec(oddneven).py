def rec(l1,l2,i,j,res):
    if i>=len(l1):
        return res
    if j>=len(l2):
        return rec(l1,l2,i+1,0,res)
    if l1[i]%2==0 and l2[j]%2!=0:
        res.append(l1[i]+l2[j]) 
    return rec(l1,l2,i,j+1,res)
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
print(rec(l1,l2,0,0,[]))