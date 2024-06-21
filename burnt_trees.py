def fun(l,i,j,n):
    if(i<0 or j<0 or i>=n or j>=n or l[i][j]!=1):
        return
    if l[i][j]==1:
        l[i][j]=2    
    fun(l,i-1,j,n) 
    fun(l,i+1,j,n)
    fun(l,i,j-1,n) 
    fun(l,i,j+1,n)
    return
l=[[0,1,1,1,0,1],[0,1,0,1,0,0],[1,0,1,1,0,0],[0,0,0,1,1,1],[1,1,0,0,0,1],[1,1,1,0,1,0]]
n=len(l)
i=3
j=5
fun(l,i,j,n)
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count=count+1
print(count) 