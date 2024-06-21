class node:
    def __init__(self):
        self.d={}
        self.flag=0
        self.d2={}
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        return t.flag==1
    def searchprex(self,pre):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
            return True
    def searchwords(self,pre):
        def dfs(node,path):
            if node.flag==1:
                l.append(path)
            for i ,j in node.d.items():
                dfs(j,path+i)
        t=self.root
        for i in pre:
            if i in t.d:
                t=t.d[i]
            else:
                return []
        l=[]
        dfs(t,pre)
        return l
    def largestword(self,l1):
        def dfs(node,path):
            if node.flag==1:
                l.append(path)
            for i ,j in node.d.items():
                dfs(j,path+i)
        t=self.root
        for j in i:
            if j in t.d:
                t=t.d[j]
            else:
                return []
        l=[]
        for i in l1:
            dfs(t,i)
        return l
    
t1=tries()
n=int(input("Enter no.of quries:"))
for i in range(n):
    a,s=input().split()
    if a=='1':
        t1.insert(s)
    if a=='2':
        print(t1.search(s))
    if a=='3':
        print(t1.searchprex(s))
    if a=='4':
        print(t1.searchwords(s))
    if a=='5':
        print(t1.largestword(s))