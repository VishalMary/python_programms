def combinations(l,k):
    def generate(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            generate(curr+[l[i]],i+1)
        return
    generate([],0)
l=[3,2,4,5,7]
k=3
combinations(l,k)
