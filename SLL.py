class node:
    def __init__(self,u):
        self.data=u
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end='->')
            t=t.next
    def addback(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def addeven(self):
        s=0
        t=self.head
        while(t!=None):
            s=s+(t.data)
        print(s)
    def addbeg(self,x):
        #if self.head==None:
         #   self.head=node(x)
        #else:
            t=node(x)
            t.next=self.head
            self.head=t
    def searchn(self,x):
        t=self.head
        while(t!=None):
            if x == t.data:
                return "Found"
            t=t.next
        return "Not Found"
    def middlenode(self):
        slow_ptr=self.head
        fast_ptr=self.head
        while(fast_ptr and fast_ptr.next):
            slow_ptr=slow_ptr.next
            fast_ptr=fast_ptr.next.next
            if(fast_ptr==None):
                return "even length"
            else:
                return "odd length"
    def subsequence(self):
        t=self.head
        c1=1
        m=0
        while(t.next!=None):
            if(t.data==t.next.data-1):
                c1=c1+1
            else:
                if c1>m:
                    m=c1
                c1=1
            t=t.next
        if c1>m:
            m=c1
        print(m)
    '''def middlenode(self):
        t=self.head
        count=0
        while(t!=None):
            count=count+1
            t=t.next
        if count%2==0:
            return "even length"
        else:
            return "odd length"
        m=(count)//2
        t=self.head
        for i in range(m):
            t=t.next
        return t.data'''
    def pairs(self):
        t=self.head
        t1=t.next
        while(t.next!=None):
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next
            t=t.next
            t1=t.next
    def bubble(self):
        T=self.head
        c=0
        p=None
        while(T.next!=None):
            f=0
            t=self.head
            while(t.next!=p):
                if(t.data>t.data):
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
                c=c+1
            if(f==0):
                break
            p=t
            T=T.next
            print(c)  
        T=self.head
        while(T!=None):
            print(T.data,end='->')
            T=T.next
        
l1=sll()
#l2=sll()
l1.head=node(7)
l1.addback(4)
l1.addback(8)
l1.addback(4)
l1.addback(2)
l1.addback(0)
l1.addback(1)
l1.addbeg(6)
#l1.display()
#l1.addback(100)
#l1.addeven()
#l2.head=node(10)
#l2.addback(200)
#print(l1.subsequence())
l1.pairs()
#print(l1.searchn(70))
#print(l1.middlenode())
print()
l1.bubble()
#l1.display()
#print()
#l2.display()
            